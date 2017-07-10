def isIn(char, aStr):
    LEN = len(aStr)
    H=LEN
    L=0
    M=(H+L)/2    
    if (aStr==''):
        return False
    elif(len(aStr)==1):
        if(aStr==char):
            return True
        else:
            return False
    else:
        if(aStr[M]==char):
            return True
        else:
            if(char < aStr[M]):
                return isIn(char,aStr[0:M])
            else:
                return isIn(char,aStr[M:LEN])
        
