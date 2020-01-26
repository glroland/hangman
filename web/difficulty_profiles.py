class DifficultyProfile():
    SYMBOLS_ALLOWED_FLAG: bool = False
    MINIMUM_LENGTH: int = 0
    MAXIMUM_LENGTH:int = 0
    LETTER_DIVERSITY: float = 0
    NAMES_ALLOWED_FLAG: bool = False

    # default constructor, abstract class
    def __init__(self):
        pass 

    # parameterized constructor 
    def __init__(self, symbolsAllowedFlag:bool, minLength:int, maxLength:int, letterDiversity: float, namesAllowedFlag: bool): 
        self.SYMBOLS_ALLOWED_FLAG = symbolsAllowedFlag
        self.MINIMUM_LENGTH = minLength
        self.MAXIMUM_LENGTH = maxLength
        self.LETTER_DIVERSITY = letterDiversity
        self.NAMES_ALLOWED_FLAG = namesAllowedFlag

    def isValidWord(self, word: str):
        # ensure string is valid and suitable for analysis first
        if not word:
            return False
        word = word.strip()
        if not word:
            return False

        # check length
        if not (self.MINIMUM_LENGTH <= len(word) <= self.MAXIMUM_LENGTH):
            return False
        
        # check symbols
        if not self.SYMBOLS_ALLOWED_FLAG and not word.isalpha():
            return False

        # check for any upper case letters, assuming they are names
        if not self.NAMES_ALLOWED_FLAG and not word.islower():
            return False
            
        # check diversity
        uniqueLetters:int = len(set(word))
        totalLetters:int = len(word)
        diversity:float = uniqueLetters / totalLetters
        if diversity < self.LETTER_DIVERSITY:
            return False
        
        # must be valid
        return True

class EasyDifficultyProfile(DifficultyProfile):
    def __init__(self):
        DifficultyProfile.__init__(self, symbolsAllowedFlag = False, minLength = 5, maxLength = 10, letterDiversity = 0.8, namesAllowedFlag = False)

class MediumDifficultyProfile(DifficultyProfile):
    def __init__(self):
        DifficultyProfile.__init__(self, symbolsAllowedFlag = False, minLength = 5, maxLength = 10, letterDiversity = 0.8, namesAllowedFlag = False)


class HardDifficultyProfile(DifficultyProfile):
    def __init__(self):
        DifficultyProfile.__init__(self, symbolsAllowedFlag = False, minLength = 5, maxLength = 10, letterDiversity = 0.8, namesAllowedFlag = False)


