class Player:

    def __init__(self, name, gender, race):
        self.name = name
        self.gender = gender
        self.race = race
        self.backpack = []
        self.equipment = []
        self.hp
        self.mp
        self.skills

    def get_p_name(self):
        return self.name

    def get_p_gender(self):
        return self.gender

    def get_p_race(self):
        return self.race

    def __str__(self):
        return "[NAME: %s | GENDER: %s | RACE: %s]" % (self.name, self.gender, self.race)
