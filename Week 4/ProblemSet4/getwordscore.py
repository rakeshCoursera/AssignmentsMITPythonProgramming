SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
word = 'Rakesh'
n=6
def getWordScore(word, n):
    word =word.lower()
    #print word
    L = len(word)
    SUM =0
    Total = 0
    for i in range(L):
        Total = Total + SCRABBLE_LETTER_VALUES[word[i]]
        #print Total
    Total = Total * L
    #print Total
    if(L==n):
        Total = Total + 50   
    return Total   
