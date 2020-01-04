import random


def start():
    print("********************")
    print("  GUESS NUMBER APP")
    print("********************")


def get_number_to_guess():
    number_to_guess = random.randint(0, 100)
    return number_to_guess


def get_user_number():

    user_number = None

    while not user_number:
        try:
            user_number = input("Guess a number between 0 and 100: ")

            if not user_number:
                continue

            user_number = int(user_number)

            if user_number < 0 or user_number > 100:
                user_number = None
                print("A number must be between 0 and 100")

        except ValueError:
            print("Write an integer number!!!!")
            user_number = None

    return user_number


def test_if_guess(user_num, comp_num):
    if user_num == comp_num:
        print("Congratulation! YOU WIN!!! The number was {}".format(comp_num))
        return True
    elif user_num < comp_num:
        print("Sorry, but {} is LOWER than the number".format(user_num))
        return False
    elif user_num > comp_num:
        print("Sorry, but {} is HIGHER than the number".format(user_num))
        return False
    else:
        print("Sorry, but something go wrong")
        return False


def main():
    start()
    number_to_guess = get_number_to_guess()
    guess_result = False
    while not guess_result:
        user_number = user_number = get_user_number()
        guess_result = test_if_guess(user_number, number_to_guess)


if __name__ == "__main__":
    main()
