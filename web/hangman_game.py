from .settings import HANGMAN_MAX_INCORRECT_GUESSES
import array

class HangmanGame():
    solution:str = None
    gameBoard:array = None
    previousGuesses:set = []
    incorrectGuessCounter:int = 0

    # parameterized constructor 
    def __init__(self, answer:str): 
        if answer:
            self.solution = answer.upper()
            self.gameBoard = [" "] * len(self.solution)
            previousGuesses = set()
            incorrectGuessCounter = 0
    
    def guessLetter(self, guess:str):
        print ("<Before> Game Board = '" + "".join(self.gameBoard) + "', Guesses = " + str(self.incorrectGuessCounter))
        foundFlag:bool = False
        if guess:
            guess = guess.upper()

            if guess not in self.previousGuesses:
                self.previousGuesses.append(guess)

                letterIndex:int = 0
                for letter in self.solution:
                    if letter == guess:
                        self.gameBoard[letterIndex] = letter
                        foundFlag = True

                    letterIndex += 1
                
                if not foundFlag:
                    self.incorrectGuessCounter += 1
        
        print ("<After> Game Board = '" + "".join(self.gameBoard) + "', Guesses = " + str(self.incorrectGuessCounter))
        return foundFlag

    def isGameOver(self):
        if self.incorrectGuessCounter >= HANGMAN_MAX_INCORRECT_GUESSES:
            return True

        return False

    def getGameBoardAsString(self):
        gameBoardString:str = "".join(self.gameBoard)
        gameBoardString = gameBoardString.replace(" ", "_")
        return gameBoardString