# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import os
import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = os.path.join(os.path.dirname(__file__), "words.txt")


def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    # print(" ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)


# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()


def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    for c in secret_word:
        if c not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    progress = list(secret_word)
    for i in range(len(progress)):
        if progress[i] not in letters_guessed:
            progress[i] = "*"
    return "".join(progress)


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    available = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    for i in letters_guessed:
        if i in available:
            available.remove(i)
    return "".join((available))


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """

    letters_in_secret_word = len(secret_word)
    VOWELS = ["a", "e", "i", "o", "u"]
    GUESSES = 10
    letters_guessed = []
    attempts = 0
    total_score = 0
    progress = lambda: get_word_progress(secret_word, letters_guessed)

    # Initialize game
    print(
        f"Welcome to hangman!\n"
        f"I am thinking of a word that is {letters_in_secret_word} letters long.\n"
        f"--------------"
    )
    # START ENGINElen(se)
    while GUESSES > 0:
        attempts += 1
        print(
            f"You have {GUESSES} guesses left.\n"
            f"Available letters: {get_available_letters(letters_guessed)}"
        )
        choice = input(f"Please guess a letter: ").lower()
        # MULTIPLE LETTER ENTRY HANDLER
        if len(choice) > 1:
            print(f"Please enter one letter at a time\n")
        # REDUNDANT LETTER HANDLER
        if choice in letters_guessed:
            print(f"Oops! You've already guessed that letter: {progress()}")
        # WITH HELP
        elif choice == "!" and with_help:
            if GUESSES < 3:
                print(
                    f"Sorry, you need at least 3 guesses to use help ('!')\n"
                    f"{progress()}\n"
                    f"--------------"
                )
            else:
                available = set(secret_word).difference(set(letters_guessed))
                available = list(available)
                new = random.randint(0, len(available) - 1)
                revealed_letter = available[new]
                letters_guessed.append(revealed_letter)
                print(
                    f"Letter revealed: {revealed_letter}\n"
                    f"{progress()}\n"
                    f"--------------"
                )
                GUESSES -= 3
                if has_player_won(secret_word, letters_guessed):
                    total_score = (GUESSES + (4 * len(set(secret_word)))) + (
                        3 * len(secret_word)
                    )
                    print(
                        f"Congratulations, you won!\n"
                        f"Your total score for this game is {total_score}"
                    )
                    break
        # INVALID CHARACTER HANDLER
        elif (
            choice not in get_available_letters(letters_guessed)
            and choice not in secret_word
        ):
            print(
                f"Oops! That is not a valid letter. Please input a letter from the alphabet: {progress()}\n"
                f"--------------"
            )

        # VALID CHOICES
        # CORRECT LETTER
        else:
            letters_guessed.append(choice)
            if choice in secret_word:
                print(f"Good guess: {progress()}")
                if has_player_won(secret_word, letters_guessed):
                    total_score = (GUESSES + (4 * len(set(secret_word)))) + (
                        3 * len(secret_word)
                    )
                    print(
                        f"--------------\n"
                        f"Congratulations, you won!\n"
                        f"Your total score for this game is {total_score}"
                    )
                    break
                else:
                    print(f"--------------")
            # INCORRECT LETTER
            else:
                print(
                    f"Oops! That letter is not in my word: {progress()}\n"
                    f"--------------"
                )
                if choice not in VOWELS:
                    GUESSES -= 1
                else:
                    GUESSES -= 2

            if GUESSES <= 0:
                print(f"Sorry, you ran out of guesses. The word was {secret_word}.")
                break


if __name__ == "__main__":

    # secret_word = choose_word(wordlist)
    secret_word = "wildcard"
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass
