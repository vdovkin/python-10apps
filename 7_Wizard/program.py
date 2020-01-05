from actors import Wizard, Creature
import random
import time


def main():
    start()
    name = get_wizard_name()

    creatures = [
        Creature("Toad", 1),
        Creature("Frog", 2),
        Creature("Bird", 3),
        Creature("Monkey", 4),
        Creature("Fox", 5),
        Creature("Bat", 6),
        Creature("Dog", 7),
        Creature("Bear", 8),
        Creature("Wolf", 9),
        Creature("Tiger", 10),
        Creature("Dragon", 20),
        Creature("Evil Wizard", 30),
    ]

    hero = Wizard(name)

    while True:

        active_creature = random.choice(creatures)
        print(
            "A {} of level {} has apper from a dark".format(
                active_creature.name, active_creature.level
            )
        )

        cmd = None
        while not cmd:
            cmd = input("Do you want to [a]ttack or [l]ook around? ").strip().lower()
            if cmd == "a":
                if hero.attack(active_creature):
                    creatures.remove(active_creature)
                else:
                    print("The wizard runs and hides taking time to recover...")
                    time.sleep(5)
                    print("The wizard returns revitalized")
            elif cmd == "l":
                continue
            elif cmd == "x":
                print("Goodbye")
                exit()
            else:
                cmd = None

        if not creatures:
            print("You've defeated all the creatures. You WIN!!!")
            break


def start():
    print("********************")
    print("  wizard game app")
    print("********************")


def get_wizard_name():
    while True:
        name = input("Plese enter the name of your wizard: ")
        if name:
            return name


if __name__ == "__main__":
    main()

