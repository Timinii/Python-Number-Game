"""A numbers guessing game"""
# import randrange module.
from random import randrange
import string

# assign default prompt.
prompt = '> '
guess_count = 0
guessed_correct = False


def choose_difficulty():
    # set global variables.
    global attempts


    while True:
        print("\nChoose a difficulty between easy, medium, and hard.")
        # collect user input into variable.
        choice = input(prompt)

        if choice == "easy":
            print(f"You chose {choice} mode.")
            easy()
            break

        elif choice == "medium":
            print(f"You chose {choice} mode.")
            medium()

            break
        elif choice == "hard":
            print(f"You chose {choice} mode.")
            hard()
            break
        else:
            print("Invalid entry.")


def easy():
    # set global variables.
    global attempts, guess_range, secret_num

    # create variable to store allowed no of attempts.
    attempts = 6
    # create variable to store allowed guess range.
    guess_range = range(1,11)
    # create variable to store randomly selected number as guess.
    secret_num = randrange(1,11)
    # show user attempts allowed.
    print(f"You have {attempts} attempts.")


def medium():
    # set global variables.
    global attempts, guess_range, secret_num

    # create variable to store allowed no of attempts.
    attempts = 4
    # create variable to store allowed guess range.
    guess_range = range(1,21)
    # create variable to store randomly selected number as guess.
    secret_num = randrange(1,21)
    # show user attempts allowed.
    print(f"You have {attempts} attempts.")


# define 'hard' function.
def hard():
    # set global variables.
    global attempts, guess_range, secret_num

    # create variable to store allowed no of attempts.
    attempts = 3
    # create variable to store allowed guess range.
    guess_range = range(1,51)
    # create variable to store randomly selected number as guess.
    secret_num = randrange(1,51)
    # show user attempts allowed.
    print(f"You have {attempts} attempts.")


def start():
    while guessed_correct == False:
        print("\nWelcome to a modified numbers guessing game!")
        choose_difficulty()
        guess_num()
        try_again()


def guess_num():
    # set global variables.
    global guess_count, attempts, guessed_correct, guess_range

    # create conditional while loop.
    while guess_count < attempts and not guessed_correct:

        try:
            print(f"\nGuess a number between {guess_range[0]} and {guess_range[-1]}.")
            # collect user input into 'guess' variable
            guess = int(input(prompt))

            if guess == secret_num:
                print("You got it right!")
                # assign boolean value to 'guessed_correct' variable.
                guessed_correct = True
            elif guess != secret_num and guess in guess_range:
                print("\nThat was wrong")
                guess_count += 1
                print(f"{attempts - guess_count} attempts left")
            elif guess not in guess_range:
                print("You guessed out of your scope. Try again!")


        except ValueError:
            print("Invalid entry. Please input a number")
    if not guess_count < attempts:
        print('\nGame over')

def try_again():
    # set global variables.
    global guessed_correct, guesscount

    while True:
        print("\nWould you like to play again? yes/no")
        # collect user input into 'go_again' variable.
        go_again = input(prompt)
        if go_again == "yes" or go_again == "y":
            # assign boolean value to 'guessed_correct' variable.
            guessed_correct = False
            # assign value to guess_count.
            guess_count = 0
            # call the 'start' function.
            start()

        elif go_again == "no" or go_again == "n":
            print("\nThanks for playing! Come back some other time.\n")
            exit(0)
        else:
            print("Invalid entry.")


# call start function
start()
