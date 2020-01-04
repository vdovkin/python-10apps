import datetime

now_date = datetime.datetime.now()


def start():
    print("********************")
    print("  Birthday app")
    print("********************")


def get_birthday_date():

    year = None
    while not year:
        year = input("What year were you born [YYYY]? ")

        if not year:
            continue

        try:
            year = int(year)
        except ValueError:
            print("Write an integer number!!!!")
            year = None
            continue
        except Exception as ex:
            print(ex)
            exit()

        if year > now_date.year:
            print("Year can't be bigger than current")
            year = None
        elif year < 1870:
            print(
                "Year can't be less than 1870 (year of birthday of the oldest person)"
            )
            year = None

    month = None
    while not month:
        month = input("What month you born [MM]? ")

        if not month:
            continue

        try:
            month = int(month)
        except ValueError:
            print("Write an integer number!!!!")
            month = None
            continue
        except Exception as ex:
            print(ex)
            exit()

        if month > 12 or month < 1:
            print("Month must be from 1 (January) to 12 (December)")
            month = None

    day = None
    while not day:
        day = input("What day you born [DD]? ")

        if not day:
            continue

        try:
            day = int(day)
        except ValueError:
            print("Write an integer number!!!!")
            day = None
            continue
        except Exception as ex:
            print(ex)
            exit()

        if day > 31 or day < 1:
            print("Day must be from 1 to 31")
            day = None
    try:
        birthday = datetime.date(year, month, day)
        return birthday
    except Exception:
        print("Something wrong with your data. Sorry")
        exit()


def differents(birthday):
    birthday_j = int(birthday.strftime("%j"))
    now_date_j = int(now_date.strftime("%j"))
    diff_days = birthday_j - now_date_j
    if diff_days == 0:
        print("Today is your birthday. Congratilations!!!")
    elif diff_days > 0:
        print("Your birthday will be in {} days".format(diff_days))
    elif diff_days < 0:
        print("Your birthday was {} days ago".format(diff_days))
    else:
        print("Something is wrong. Sorry")


def main():
    start()
    birthday = get_birthday_date()
    print("You were born on {}".format(birthday.strftime("%d/%m/%Y")))
    differents(birthday)


if __name__ == "__main__":
    main()
