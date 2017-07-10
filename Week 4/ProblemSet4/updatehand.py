hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
word = 'quail'
def updateHand(hand, word):
    seq = hand.copy()
    for i in range(len(word)):
        if(word[i] in seq and seq[word[i]]>0):
            seq[word[i]] = seq.get(word[i],0)-1
    return seq,hand


def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line
