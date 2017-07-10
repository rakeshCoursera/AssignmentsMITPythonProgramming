secretWord = 'apple'
lettersGuessed = ['a', 'i', 'k', 'p', 'l', 'e']
def isWordGuessed(secretWord, lettersGuessed):
    for i in secretWord:
        print i
        if (i in lettersGuessed):
            continue;
        else:
            return False
    return True
                   
        
