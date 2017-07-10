hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
word ='quaila'

def isValidWord(word, hand,wordList):
    seq = hand.copy()
    if(word == ''):
        return False
    else:
        for i in range(len(word)):
            if(word[i] in seq and seq[word[i]]>0):
                seq[word[i]] = seq.get(word[i],0)-1
                a=0
            else:
                a=1
                break
        print a
        if(word in wordList and a==0):
            return True
        else:
            return False
        
        
    
