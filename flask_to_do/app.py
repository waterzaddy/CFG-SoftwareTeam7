from flask import Flask, render_template, request, redirect, url_for
from classes import VirtualPet

""" VARIABLES """

app = Flask(__name__, template_folder="templates")

todos = [{"task": "Sample task", "done": False}]

pet_name = "Gizmo"
pet = VirtualPet(pet_name)

health_counter = 1
happiness_counter = 0

""" APP ROUTE + ADD, EDIT, DELETE, CHECK FUNCTIONS"""


@app.route("/")
def index():
    return render_template("index.html", todos=todos, health_counter=health_counter)


@app.route("/add", methods=["POST"])
def add():
    todo = request.form["todo"]
    todos.append({"task": todo, "done": False})
    return redirect(url_for("index"))


@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo["task"] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)


@app.route("/check/<int:index>")
def check(index):
    todos[index]["done"] = not todos[index]["done"]
    #### need to figure out this bit. How do we update the health counter? currently results in error when "complete is clicked"
    # water = pet.water()
    # health_counter = health_counter + water
    return redirect(url_for("index"))


@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))


""" CLASS INSTANCE """


""" RUN APP """
if __name__ == "__main__":
    app.run(debug=True)
