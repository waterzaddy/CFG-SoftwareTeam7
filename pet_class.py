class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.happiness = 100

    def feed(self):
        self.health += 10
      
    def water(self):
        self.health += 10
      
    def play(self):
        self.happiness += 10

    def perform_self_care_actions(self, action1=False, action2=False, action3=False):
        if action1:
            self.health += 5
        if action2:
            self.happiness += 5
        if action3:
            self.happiness += 10

    def get_status(self):
        return {
            "name": self.name,
            "health": self.health,
            "happiness": self.happiness
        }

# Example usage:
if __name__ == "__main__":
    # Create a virtual pet
    pet_name = "Gizmo"
    pet = VirtualPet(pet_name)

    # Simulate self-care actions
    pet.perform_self_care_actions(action1=True, action2=True, action3=True)
    pet.feed()
    pet.play()

    # Get the virtual pet's status
    pet_status = pet.get_status()
    print(f"{pet_status['name']}'s Health: {pet_status['health']}")
    print(f"{pet_status['name']}'s Happiness: {pet_status['happiness']}")
