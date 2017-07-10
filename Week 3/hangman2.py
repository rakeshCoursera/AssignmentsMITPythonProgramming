secretWord = 'broccoli'
lettersGuessed = ['d', 'b', 'w', 'c', 'a', 'v', 'k', 'y', 'u', 'r']
def getGuessedWord(secretWord, lettersGuessed):
    word =''
    for i in secretWord:
        print i
        if (i in lettersGuessed):
            word = word + i
        else:
            word =word + '_ '
    return word
