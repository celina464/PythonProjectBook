
"""
//    log.debug("The function is a game of hangman with a pre-defined list of words and includes graphics for the")
//    log.debug("The function is a game of hangman with a pre-defined list of words and includes graphics for the")
//    hangman, scoring, and the ability to play again.
//    
//    :param hangman: A list of strings representing the different stages of the hangman graphic to be
//    printed during the game
//    :return: The code does not have any output as it contains only function and class definitions. It
//    does not have any function calls or executable code outside of the function definitions.
//   """

from random import *

player_score = 0
computer_score = 0

def hangedman(hangman):
    #log.debug("hangman is %s", hangman)
    graphic = [
        """
            +-------+
            |
            |
            |
            |
            |
            ==============
        """,
        """
            +-------+
            |       |
            |       O
            |
            |
            |
            ==============
        """,
        """
            +-------+
            |       |
            |       O
            |       |
            |
            |
            ==============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|
            |
            |
            ==============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|-
            |
            |
            ==============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|-
            |      /
            |
            ==============
        """,
        """
            +-------+
            |       |
            |       O
            |      -|-
            |      / \
            |
            ==============
        """]
    print(graphic[hangman])
    return


    
def guess_letter():
    """
    This function prompts the user to guess a letter for a mystery word and returns the guessed letter
    in lowercase after stripping any whitespace.
    :return: The letter guessed by the user after being stripped of any leading or trailing white space
    and converted to lowercase.
    """
    print
    letter = input("Take a guess at our mystery word: ")
    letter.strip()
    letter.lower()
    print
    return letter
    
def play_again():
    """
    The function asks the user if they want to play again and returns their answer if it is "y", "Y",
    "yes", "Yes", or "Of course!", otherwise it prints a message thanking them for playing.
    :return: the user's input if it is "y", "Y", "yes", "Yes", or "Of course!". If the input is anything
    else, the function does not return anything, but prints a message thanking the user for playing the
    game.
    """
    answer = input("Would you like to play again? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "Of course!"):
        return answer
    else:
        print ("Thank you very much for playing our game. See you next time!")
    
def scores():
    """
    The function "scores" prints the high scores of the player and computer.
    """
    global player_score, computer_score
    print ("HIGH SCORES")
    print ("Player: ",player_score)
    print ("Computer: ",computer_score)


def start():
    """
    The function starts a game of Linux Hangman and keeps playing until the user decides to quit, then
    displays the scores.
    """
    print ("Let's play a game of Linux Hangman.")
    while game():
        pass
    scores()

def game():  # sourcery skip: low-code-quality
    """
    This function is a simple hangman game where the player has to guess a randomly chosen word from a
    list of words.
    :return: The function `play_again()` is being returned.
    """
    dictionary = ["gnu”,”kernel”,”linux”,”mageia”,"penguin”,”ubuntu”]
    word = choice(dictionary)
    word_length = len(word)
    clue = word_length * [""]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score
    
# This is the main game loop for the hangman game. It checks if the number of wrong guesses is less
# than the maximum allowed tries and if the current guessed word is not equal to the actual word. It
# then prompts the user to guess a letter using the `guess_letter()` function and checks if the input
# is a single letter and an alphabet. If the letter has already been guessed, it prints a message
# saying so. If the letter is not in the word, it increments the number of wrong guesses and prints a
# message saying so. If the letter is in the word, it updates the `clue` list with the correct
# letter(s) and prints a message saying so. Finally, it prints the hangman graphic, the current state
# of the `clue` list, and the letters guessed so far. If the number of wrong guesses equals the
# maximum allowed tries, it prints a message saying the game is over and increments the computer's
# score. If the current guessed word is equal to the actual word, it prints a message saying the
# player has won and increments the player's score. It then returns the result of the `play_again()`
# function.
    while (letters_wrong != tries) and ("".join(clue) != word):
        letter=guess_letter()
        if len(letter)==1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print("You've already picked", letter)
            else:
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong += 1
                    print ("Sorry,", letter, "isn't what we're looking for.")
                else:
                    print("Congratulations,", letter, "is correct.")
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print("Choose another.")
            
        hangedman(letters_wrong)
        print("".join(clue))
        print("Guesses: ", letters_tried)
        
        if letters_wrong == tries:
            print("Game Over.")
            print("The word was", word)
            computer_score += 1
            break
        if "".join(clue) == word:
            print ("You Win!")
            print ("The word was", word)
            player_score += 1
            break
        
    return play_again()


if __name__ == '__main__':
    start()
