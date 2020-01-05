import random


class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature {} of lever {}".format(self.name, self.level)

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.expiriense = 0

    def attack(self, creature):
        print("The wizard {} attack {}!".format(self.name, creature.name))

        my_roll = self.get_defensive_roll()
        creature_roll = creature.get_defensive_roll()

        print("You roll {}..".format(my_roll))
        print("{} roll {}...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            points = creature.level * 10
            self.add_expirience(points)
            print("The wizard is win!")
            print("You got {} expiriense points".format(points))
            while self.is_level_up(self.expiriense, self.level):
                self.level += 1
                print("you got a new level {}".format(self.level))
            return True
        else:
            print("You lost a battle")
            return False

    def add_expirience(self, points):
        self.expiriense += points

    def is_level_up(self, points, level):
        points_to_new_level = level * round(10 * 1.05 ** level)
        if points_to_new_level <= points:
            return True
        else:
            return False

