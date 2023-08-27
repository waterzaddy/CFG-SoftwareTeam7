from flask import Flask, render_template, request, redirect, url_for, session, flash
from classes import VirtualPet
from functions import get_inspirational_quote, todo_length, task_length
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

""" VARIABLES """

app = Flask(__name__, template_folder="templates")
app.config.from_object("config.Config")

todos_health = [{"task": "Sample task", "done": False}]
todos_happiness = [{"task": "Sample task", "done": False}]

# Initialize APScheduler for background decay while app is running
scheduler = BackgroundScheduler()
scheduler.start()


""" CLASS INSTANCES """

# Create an instance of VirtualPet
pet = VirtualPet("Your Virtual Pet", health=40, happiness=40)


# Scheduled decay task
def scheduled_decay():
    pet.decay()


try:
    # Add scheduled decay task to run every 30 minutes
    scheduler.add_job(scheduled_decay, trigger='interval', minutes=30)
except Exception as e:
    print("Ooops! Something went wrong when monitoring your pet's vitals over time:", e)


""" APP ROUTES """


@app.route("/")
def index():
    if "user" in session:
        user = session["user"]

        # Calculate elapsed time since last login
        if "last_login" in session:
            last_login_time = session["last_login"]
            current_time = datetime.now()
            elapsed_time = current_time - last_login_time

            # Calculate decay based on elapsed time and apply to pet's health and happiness
            pet.decay_between_sessions(elapsed_time.total_seconds())

            # Update last login time
            session["last_login"] = current_time

        return render_template("index.html", todos_health=todos_health, todos_happiness=todos_happiness, pet=pet, user=user)
    else:
        return render_template("index.html", todos_health=todos_health, todos_happiness=todos_happiness, pet=pet)


""" LOGIN / LOGOUT / SESSIONS """


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("index"))
    else:
        if "user" in session:
            return redirect(url_for("index"))
        return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


""" HEALTH: ADD, EDIT, DELETE, CHECK FUNCTIONS"""


@app.route("/add_health", methods=["POST"])
def add_health():
    try:
        if todo_length(todos_health):
            todo = request.form["todo"]
            if task_length(todo):
                print(todo)
                todos_health.append({"task": todo, "done": False})
            else:
                flash("Tasks must be between 1 and 40 characters")
        else:
            flash("You can have a maximum of 10 tasks at the time")
    except Exception as e:
        # Handle any exceptions that might occur and provide a user-friendly error message
        error_message = "Ooops! An error occurred: " + str(e)
        flash(error_message, "error")

    return redirect(url_for("index"))



@app.route("/edit_health/<int:index>", methods=["GET", "POST"])
def edit_health(index):
    todo = todos_health[index]
    if request.method == "POST":
        todo["task"] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit_health.html", todo=todo, index=index)


@app.route("/check_health/<int:index>")
def check_health(index):
    todos_health[index]["done"] = not todos_health[index]["done"]
    if pet.max_status >= pet.health >= pet.min_status:
        if todos_health[index]["done"]:
            pet.health = min(pet.max_status, pet.health + 5)
        else:
            pet.health = min(pet.max_status, pet.health - 5)
    return redirect(url_for("index", pet=pet))


@app.route("/delete_health/<int:index>")
def delete_health(index):
    if todos_health[index]["done"]:
        pet.health = min(pet.max_status, pet.health - 5)
    del todos_health[index]
    return redirect(url_for("index", pet=pet))


""" HAPPINESS: ADD, EDIT, DELETE, CHECK FUNCTIONS """


@app.route("/add_happiness", methods=["POST"])
def add_happiness():
    try:
        if todo_length(todos_happiness):
            todo = request.form["todo"]
            if task_length(todo):
                print(todo)
                todos_happiness.append({"task": todo, "done": False})
            else:
                flash("Tasks must be between 1 and 40 characters")
        else:
            flash("You can have a maximum of 10 tasks at the time")
    except Exception as e:
        # Handle any exceptions that might occur and provide a user-friendly error message
        error_message = "Ooops! An error occurred: " + str(e)
        flash(error_message, "error")

    return redirect(url_for("index"))



@app.route("/edit_happiness/<int:index>", methods=["GET", "POST"])
def edit_happiness(index):
    todo = todos_happiness[index]
    if request.method == "POST":
        todo["task"] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit_happiness.html", todo=todo, index=index)


@app.route("/check_happiness/<int:index>")
def check_happiness(index):
    todos_happiness[index]["done"] = not todos_happiness[index]["done"]
    if pet.max_status >= pet.happiness >= pet.min_status:
        if todos_happiness[index]["done"]:
            pet.happiness = min(pet.max_status, pet.happiness + 5)
        else:
            pet.happiness = min(pet.max_status, pet.happiness - 5)
    return redirect(url_for("index", pet=pet))


@app.route("/delete_happiness/<int:index>")
def delete_happiness(index):
    if todos_happiness[index]["done"]:
        pet.happiness = min(pet.max_status, pet.happiness - 5)
    del todos_happiness[index]
    return redirect(url_for("index", pet=pet))


"""
BUTTONS ROUTES
"""


@app.route("/feed")
def feed():
    pet.health = min(pet.max_status, pet.health + 5)
    return redirect(url_for("index"))


@app.route("/water")
def water():
    pet.health = min(pet.max_status, pet.health + 5)
    return redirect(url_for("index"))


@app.route("/exercise")
def exercise():
    pet.health = min(pet.max_status, pet.health + 10)
    return redirect(url_for("index"))


@app.route("/hug")
def hug():
    quote = get_inspirational_quote()
    pet.happiness = min(pet.max_status, pet.happiness + 10)
    return render_template("index.html", pet=pet, quote=quote, todos_health=todos_health,
                           todos_happiness=todos_happiness)


""" RUN APP """
if __name__ == "__main__":
    app.run(debug=True)
