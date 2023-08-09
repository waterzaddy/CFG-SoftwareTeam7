from flask import Flask, render_template, request, redirect, url_for
from classes import VirtualPet, Counter

""" VARIABLES """

app = Flask(__name__, template_folder="templates")

todos_health = [{"task": "Sample task", "done": False}]
todos_happiness = [{"task": "Sample task", "done": False}]

""" CLASS INSTANCES """

# creating pet instance. not in use yet (to be used for booster buttons)
pet = VirtualPet("Gizmo")
# creating instance for health/happiness counters. Variables can't be reassigned so this needs to be through classes
counter = Counter()


""" APP ROUTES """


@app.route("/")
def index():
    return render_template("index.html", todos_health=todos_health, todos_happiness=todos_happiness, health_counter=counter.health_counter, happiness_counter=counter.happiness_counter)


""" HEALTH: ADD, EDIT, DELETE, CHECK FUNCTIONS"""


@app.route("/add_health", methods=["POST"])
def add_health():
    todo = request.form["todo"]
    todos_health.append({"task": todo, "done": False})
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
    if counter.max_value > counter.health_counter >= counter.min_value:
        if todos_health[index]["done"]:
            counter.health_counter += 1
        else:
            counter.health_counter -= 1
    else:
        pass
    return redirect(url_for("index", health_counter=counter.health_counter))


@app.route("/delete_health/<int:index>")
def delete_health(index):
    if todos_health[index]["done"]:
        counter.health_counter -= 1
    else:
        pass
    del todos_health[index]
    return redirect(url_for("index"))


""" HAPPINESS: ADD, EDIT, DELETE, CHECK FUNCTIONS """


@app.route("/add_happiness", methods=["POST"])
def add_happiness():
    todo = request.form["todo"]
    todos_happiness.append({"task": todo, "done": False})
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
    if counter.max_value > counter.happiness_counter >= counter.min_value:
        if todos_happiness[index]["done"]:
            counter.happiness_counter += 1
        else:
            counter.happiness_counter -= 1
    else:
        pass
    return redirect(url_for("index", happiness_counter=counter.happiness_counter))


@app.route("/delete_happiness/<int:index>")
def delete_happiness(index):
    del todos_happiness[index]
    return redirect(url_for("index"))


""" RUN APP """
if __name__ == "__main__":
    app.run(debug=True)
