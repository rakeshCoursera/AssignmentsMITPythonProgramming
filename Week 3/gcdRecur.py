def gcdRecur(a, b):
    if(a==0 or b==0):
        if(a==0):
            return b
        if(b==0):
            return a
    else:
        if(a==b):
            return a
        elif(a>b):
            return gcdRecur(b, a%b)
        else:
            return gcdRecur(a, b%a)
