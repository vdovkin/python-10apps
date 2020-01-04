def start():
    print("********************")
    print("    HELLO APP   ")
    print("********************")


def get_name():

    name = None

    while not name:
        try:
            name = input("What is your name? ")
        except Exception:
            print("Somethin is wrong")

    return name


def grettings(name):
    print("Hello, {}".format(name))


def main():
    start()
    name = get_name()
    grettings(name)


if __name__ == "__main__":
    main()
