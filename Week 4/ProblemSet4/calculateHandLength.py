hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1, 't':1,'s':1}
def calculateHandlen(hand):
    total = 0
    for i in dict.values(hand):
        total = total + i
    return total
