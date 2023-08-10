from flask import Flask, render_template, redirect, url_for
from classes import VirtualPet, Counter
import requests

app = Flask(__name__, static_folder='static')

# Define the VirtualPet class
class VirtualPet:
    def __init__(self, name, health=100, happiness=100):
        self.name = name
        self.max_status = 100
        self.min_status = 5
        self.health = min(self.max_status, max(self.min_status, health))  # Ensure health is within range
        self.happiness = min(self.max_status, max(self.min_status, happiness))  # Ensure happiness is within range

    def decay(self):
        decay_rate = 0.1
        self.health = max(self.min_status, self.health - decay_rate)
        self.happiness = max(self.min_status, self.happiness - decay_rate)

counter = Counter()

pet = VirtualPet("Your Virtual Pet")
pet = VirtualPet("Your Virtual Pet", health=40, happiness=40)
counter = Counter()

@app.route("/")
def index():
    return render_template("index.html", pet=pet)


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

# Function to get a random inspirational quote from the API
def get_inspirational_quote():
    category = 'inspirational'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    api_key = 'Zu3DasmIkTOY9/xNQFPEDg==zSkWG4DY0AS1S3Av'

    response = requests.get(api_url, headers={'X-Api-Key': api_key})

    if response.status_code == requests.codes.ok:
        quote_data = response.json()
        random_quote = quote_data[0]['quote']
        return random_quote
    else:
        return "Error fetching quote"

@app.route("/hug")
def hug():
    quote = get_inspirational_quote()
    pet.happiness = min(pet.max_status, pet.happiness + 10)
    return render_template("index.html", pet=pet, quote=quote)

if __name__ == "__main__":
    app.run(debug=True)
