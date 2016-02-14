class Player:

    def __init__(self, name, gender, race):
        self.name = name
        self.gender = gender
        self.race = race['Title']
        self.backpack = []
        self.weapon = race['Weapon']
        self.armor = race['Armor']
        self.attk = race['Attk']
        self.defe = race['Def']
        self.hp = race['Hp']
        self.mp = race['Mp']
        self.skills = race['Skills']

    def get_p_name(self):
        return self.name

    def get_p_gender(self):
        return self.gender

    def get_p_race(self):
        return self.race

    def get_p_backpack(self):
        return self.backpack

    def get_p_weapon(self):
        return self.weapon

    def get_p_armor(self):
        return self.armor

    def get_p_attk(self):
        return self.attk

    def get_p_def(self):
        return self.defe

    def get_p_hp(self):
        return self.hp

    def get_p_mp(self):
        return self.mp

    def get_p_skills(self):
        return self.skills

    def __str__(self):
        return "[NAME: %s | GENDER: %s | RACE: %s | HP: %s | MP: %s | Weapon: %s | Armor: %s | Attk: %s" \
               " | Def: %s | Skills %s]" % \
               (self.name, self.gender, self.race, self.hp, self.mp, self.weapon, self.armor, self.attk, self.defe,
                self.skills)
