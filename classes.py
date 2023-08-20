class VirtualPet:
    def __init__(self, name, health=100, happiness=100):
        self.name = name
        self.max_status = 60
        self.min_status = 5
        self.health = min(self.max_status, max(self.min_status, health))  # Ensure health is within range
        self.happiness = min(self.max_status, max(self.min_status, happiness))  # Ensure happiness is within range

    def decay(self, decay_rate=0.1):
        self.health = max(self.min_status, self.health - decay_rate)
        self.happiness = max(self.min_status, self.happiness - decay_rate)

    def decay_between_sessions(self, elapsed_time_in_seconds):
        decay_rate_between_sessions = 0.05  # can be adjusted
        decay_amount = decay_rate_between_sessions * (elapsed_time_in_seconds / (60 * 60 * 24))  # Assuming 1 day
        self.health = max(self.min_status, self.health - decay_amount)
        self.happiness = max(self.min_status, self.happiness - decay_amount)


# NOT IN USE FOR NOW
# class Counter:
#     def __init__(self):
#         self.health_counter = 0
#         self.happiness_counter = 0
#         self.max_value = 100
#         self.min_value = 0