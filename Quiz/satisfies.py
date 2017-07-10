L = ['','a']

def f(s):
    return '' in s

def satisfiesF(L):
    j=0
    if(L ==[]):
        return 0
    else:
        for i in range(len(L)):
            #print i
            p = f(L[j])
            if(p ==False):
                del L[j]
                j=j-1
            else:
                print L
                j=j+1
        return len(L)
            
    
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
