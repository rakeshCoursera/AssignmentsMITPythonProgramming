def gcdIter(a, b):
    if(a>=b):
        gcd=b
    else:
        gcd=a;
    while(a%gcd >0  or b%gcd > 0 ):
        gcd -= 1
    return gcd
        
