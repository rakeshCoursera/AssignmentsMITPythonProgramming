#lettersGuessed = ['d', 'b', 'w', 'c', 'a', 'v', 'k', 'y', 'u', 'r']
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
import string
print string.ascii_lowercase
def getAvailableLetters(lettersGuessed):
    word =''
    for i in string.ascii_lowercase:
        print i
        if (i in lettersGuessed):
            continue
        else:
            word =word + i
    return word
