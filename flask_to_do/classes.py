""" CLASSES """

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.happiness = 100

    def feed(self):
        self.health += 10
        return self.health

    def water(self):
        self.health += 10
        return self.health

    def play(self):
        self.happiness += 10
        return self.happiness

    def perform_self_care_actions(self, action1=False, action2=False, action3=False):
        if action1:
            self.health += 5
        if action2:
            self.happiness += 5
        if action3:
            self.happiness += 10

    def get_status(self):
        return {"name": self.name, "health": self.health, "happiness": self.happiness}


class Counter:
    def __init__(self):
        self.health_counter = 0
        self.happiness_counter = 0
        self.max_value = 100
        self.min_value = 0
