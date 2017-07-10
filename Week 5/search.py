L =[2,5,8,4,6,1,3,4]
e = 5

def swapSort(L): 
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print L
    print "Final L: ", L

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False



def newsearch(L, e):
    size = len(L)
    print size
    for i in range(size):
        print i
        print(L[size-i-1],e)
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

