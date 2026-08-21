"""
File: hangman.py
Name: Summer
-----------------------------
This program plays a console-based Hangman game.

The user is shown a word represented by dashes and tries to
guess the hidden word by entering one character in each round.
If the guessed character is correct, the program updates and
displays the word on the console.

The player has a limited number of chances, defined by
N_TURNS, to successfully guess the word and win the game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    The player guesses letters to find out a word with limited turns.
    """
    word = random_word()
    display = ""
    for i in range(len(word)):
        display += '_'
    turns = N_TURNS
    print("The word looks like: " + display)
    print("You have " + str(turns) + " wrong guesses left.")

    while turns > 0:
        guess = input("Your guess: ")
        if len(guess) != 1:
            print("Illegal format.")
        elif not guess.isalpha():
            print("Illegal format.")
        else:
            guess = guess.upper()
            if guess not in word:
                print("There is no " + guess + "'s in the word.")
                turns -= 1
            else:
                new_display = ""
                for i in range(len(word)):
                    if guess == word[i]:
                        print("You are correct!")
                        new_display += guess
                    else:
                        new_display += display[i]
                display = new_display
            if display.isalpha():
                print("You win!!")
                print("The answer is: " + word)
                return
            if turns > 0:
                print("The word looks like: " + display)
                print("You have " + str(turns) + " wrong guesses left.")
    print("You are completely hung :( ")
    print("The answer is: " + word)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == '__main__':
    main()
