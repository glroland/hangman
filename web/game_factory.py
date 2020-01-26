import random
from .difficulty_profiles import DifficultyProfile
from .hangman_game import HangmanGame
from .dictionary import Dictionary

class GameFactory():
    
    @staticmethod
    def createGame(difficultyProfile:DifficultyProfile):
        print("Selected Difficulty Profile: " + difficultyProfile.__class__.__name__)
        
        dictionary:Dictionary = Dictionary(difficultyProfile)

        wordsInMaster:int = dictionary.countAllWordsInMaster()
        print("Words in Master Dictionary: " + str(wordsInMaster))

        gameReadyWordsInMaster:int = dictionary.countGameReadyWordsInMaster()
        print ("Game Ready Words in Master Dictionary: " + str(gameReadyWordsInMaster))

        gameReadyWords:list = dictionary.extractGameReadyWords()
        print (str(len(gameReadyWords)))
        answer:str = gameReadyWords[random.randint(0, gameReadyWordsInMaster - 1)]
        print ("Random Word = " + answer)

        return HangmanGame(answer)
