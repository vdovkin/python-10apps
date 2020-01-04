import jornal


def start():
    print("********************")
    print("  Journal app")
    print("********************")


def j_list(data):
    print("Your journal enrties: ")
    for idx, entry in enumerate(data):
        print("* [{}] {}".format(idx + 1, entry))


def j_add(data):
    print("Enter your journal entry:")
    add_text = input()
    jornal.add_entry(add_text, data)


def j_exit():
    print("exit from journal")
    exit()


def get_action():
    action = None
    while not action:
        try:
            action = input("What do you want do? [L]ist, [A]dd, E[x]it ")
            if not action.isalpha():
                action = None
                continue

            if action.lower() in ["l", "a", "x"]:
                return action.lower()
            else:
                action = None
        except Exception:
            print("something goes wrong. Sorry")
            exit()


def main():
    start()

    journal_name = "defalt"
    journal_data = jornal.load(journal_name)

    while True:

        action = get_action()

        if action == "l":
            j_list(journal_data)
        elif action == "a":
            j_add(journal_data)
        elif action == "x":
            jornal.save(journal_name, journal_data)
            j_exit()


if __name__ == "__main__":
    main()
