from .difficulty_profiles import DifficultyProfile
from .settings import HANGMAN_MASTER_DICTIONARY_FILENAME

class Dictionary():
    difficultyProfile:DifficultyProfile = None

    # parameterized constructor 
    def __init__(self, selectedDifficultyProfile:DifficultyProfile): 
        self.difficultyProfile = selectedDifficultyProfile

    def countAllWordsInMaster(self):
        lineCounter:int = 0
        f = open(HANGMAN_MASTER_DICTIONARY_FILENAME, "r")
        fLines = f.readlines()
        for line in fLines:
            if line:
                lineCounter += 1
        f.close()
        return lineCounter

    def countGameReadyWordsInMaster(self):
        lineCounter:int = 0
        f = open(HANGMAN_MASTER_DICTIONARY_FILENAME, "r")
        fLines = f.readlines()
        for line in fLines:
            if line:
                if self.difficultyProfile.isValidWord(line):
                    lineCounter += 1
        f.close()
        return lineCounter

    def extractGameReadyWords(self):
        gameReadyWords:list = list()
        f = open(HANGMAN_MASTER_DICTIONARY_FILENAME, "r")
        fLines = f.readlines()
        for line in fLines:
            if line:
                line = line.strip()
                if self.difficultyProfile.isValidWord(line):
                    gameReadyWords.append(line)
        f.close()
        return gameReadyWords




