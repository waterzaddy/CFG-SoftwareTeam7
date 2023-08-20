from flask import Flask, render_template, request, redirect, url_for, session, flash
from classes import VirtualPet
from functions import get_inspirational_quote, todo_length, task_length

""" VARIABLES """

app = Flask(__name__, template_folder="templates")
app.config.from_object("config.Config")

todos_health = [{"task": "Sample task", "done": False}]
todos_happiness = [{"task": "Sample task", "done": False}]

""" CLASS INSTANCES """

pet = VirtualPet("Your Virtual Pet", health=40, happiness=40)


""" APP ROUTES """


@app.route("/")
def index():
    if "user" in session:
        user = session["user"]
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
    if todo_length(todos_health):
        todo = request.form["todo"]
        if task_length(todo):
            print(todo)
            todos_health.append({"task": todo, "done": False})
        else:
            flash("Tasks must be between 1 and 40 characters")
    else:
        flash("You can have a maximum of 10 tasks at the time")
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
    if todo_length(todos_happiness):
        todo = request.form["todo"]
        if task_length(todo):
            print(todo)
            todos_happiness.append({"task": todo, "done": False})
        else:
            flash("Tasks must be between 1 and 40 characters")
    else:
        flash("You can have a maximum of 10 tasks at the time")
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
    return render_template("index.html", pet=pet)


@app.route("/water")
def water():
    pet.health = min(pet.max_status, pet.health + 5)
    return render_template("index.html", pet=pet)


@app.route("/exercise")
def exercise():
    pet.health = min(pet.max_status, pet.health + 10)
    return render_template("index.html", pet=pet)


@app.route("/hug")
def hug():
    quote = get_inspirational_quote()
    pet.happiness = min(pet.max_status, pet.happiness + 10)
    return render_template("index.html", pet=pet, quote=quote)


""" RUN APP """
if __name__ == "__main__":
    app.run(debug=True)