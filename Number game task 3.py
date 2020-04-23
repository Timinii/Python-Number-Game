"""A numbers guessing game"""
# import randrange module.
from random import randrange
import string

# assign default prompt.
prompt = '> '
# create variable to count guesses.
guess_count = 0
# assign default boolean
guessed_correct = False


# define choose difficulty function.
def choose_difficulty():
    # set global variables.
    global attempts

    # create an infinite loop.
    while True:
        # print message to user.
        print("\nChoose a difficulty between easy, medium, and hard.")
        # collect user input into variable.
        choice = input(prompt)

        # set conditional statements to run code block.
        if choice == "easy":
            print(f"You chose {choice} mode.")
            # call 'easy' function.
            easy()
            # break out of while loop.
            break
        # set conditional statements to run code block.
        elif choice == "medium":
            print(f"You chose {choice} mode.")
            # call 'medium' function.
            medium()
            # break out of while loop.
            break
        # set conditional statements to run code block.
        elif choice == "hard":
            print(f"You chose {choice} mode.")
            # call 'hard' function.
            hard()
            # break out of while loop.
            break
        # set conditional statements to run code block.
        else:
            print("Invalid entry.")


# define 'easy' function.
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


# define 'medium' function.
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


# define 'start' function.
def start():
    # create a conditional while loop
    while guessed_correct == False:
        # print message to user.
        print("\nWelcome to a modified numbers guessing game!")
        # call 'choose difficulty' function.
        choose_difficulty()
        # call 'guess num' function.
        guess_num()
        # call 'try again' function.
        try_again()


# create 'guess num' function.
def guess_num():
    # set global variables.
    global guess_count, attempts, guessed_correct, guess_range

    # create conditional while loop.
    while guess_count < attempts and not guessed_correct:

        try:
            # print message to users.
            print(f"\nGuess a number between {guess_range[0]} and {guess_range[-1]}.")
            # collect user input into 'guess' variable
            guess = int(input(prompt))

            # create conditional if-statement.
            if guess == secret_num:
                # print message to user.
                print("You got it right!")
                # assign boolean value to 'guessed_correct' variable.
                guessed_correct = True
            # create conditional elif-statement.
            elif guess != secret_num and guess in guess_range:
                # print message to user.
                print("\nThat was wrong")
                # increment 'guess_count'.
                guess_count += 1
                # print message to user.
                print(f"{attempts - guess_count} attempts left")
            # create conditional elif-statement.
            elif guess not in guess_range:
                # print message to user.
                print("You guessed out of your scope. Try again!")
            # # create conditional else-statement.

        except ValueError:
            print("Invalid entry. Please input a number")
    if not guess_count < attempts:
        print('\nGame over')

# define 'try_again' function.
def try_again():
    # set global variables.
    global guessed_correct, guess_count

    # create infinite while loop.
    while True:
        # print message to user.
        print("\nWould you like to play again? yes/no")
        # collect user input into 'go_again' variable.
        go_again = input(prompt)
        # create conditional if-statement.
        if go_again == "yes" or go_again == "y":
            # assign boolean value to 'guessed_correct' variable.
            guessed_correct = False
            # assign value to gues_count.
            guess_count = 0
            # call the 'start' function.
            start()
        # create conditional elif-statement.
        elif go_again == "no" or go_again == "n":
            print("\nThanks for playing! Come back some other time.\n")
            # call exit function with no error message.
            exit(0)
        # create conditional else-statement.
        else:
            # print message to user.
            print("Invalid entry.")


# call start function
start()
