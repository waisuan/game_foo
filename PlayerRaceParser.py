class PlayerRaceParser:
    def __init__(self):
        self.race_titles = []
        self.races = {}
        file_object = open("db/race.txt", "r")
        file_object.readline().rstrip()  # metadata
        content = file_object.readlines()
        for race in content:
            race_details = race.rstrip().split(',')
            self.race_titles.append(race_details[0])
            race_details_table = {'Title': race_details[0], 'Attk': race_details[1], 'Def': race_details[2],
                                  'Weapon': race_details[3], 'Armor': race_details[4], 'Hp': race_details[5],
                                  'Mp': race_details[6], 'Skills': race_details[7]}
            self.races[race_details[0]] = race_details_table

    def get_race_titles(self):
        return self.race_titles

    def get_races(self):
        return self.races
