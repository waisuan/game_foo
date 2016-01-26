from Player import Player


def get_player_name():
    player_name = ""
    while player_name == "":
        player_name = raw_input("What is your name? ")
        if player_name == "":
            print_i_didnt_quite_catch_that()
    print "Hello, %s!" % player_name
    return player_name


def get_player_gender():
    player_gender = ""
    while player_gender != "m" and player_gender != "f":
        player_gender = raw_input("Are you male (m) or female (f)? ").lower()
        if player_gender != "m" and player_gender != "f":
            print_i_didnt_quite_catch_that()
    return player_gender.upper()


def get_player_race():
    player_race_options = ["War Orc", "Paladin", "Arcanist", "Lancer", "Hunter"]
    print "Please pick a RACE before we can officially begin!"
    index = 1
    for race in player_race_options:
        print "%i) %s" % (index, race)
        index += 1
    player_race = "null"
    while (player_race.isdigit() and (int(player_race) < 1 or int(player_race) > len(player_race_options))) \
        or (player_race.isalpha() and player_race.title() not in player_race_options) \
            or player_race == "":
        player_race = raw_input("I choose: ")
        if player_race.isdigit() and (1 <= int(player_race) <= len(player_race_options)):
            return player_race
        elif player_race.replace(" ", "").isalpha() and player_race != "":
            player_race = player_race.title()
            for race in player_race_options:
                if player_race == race:
                    return player_race
        player_race = "null"
        print_i_didnt_quite_catch_that()


def print_great():
    print "Great!"


def print_i_didnt_quite_catch_that():
    print "Oops, I didn't quite catch that..."


def get_starting_point():
    print "Choose a starting point."


print """
        Welcome to IXION!\n
        A simple & fun text-based game created in Python.\n
        Let's begin...
        """
player = Player(get_player_name(), get_player_gender(), get_player_race())
print_great()
print player
get_starting_point()

