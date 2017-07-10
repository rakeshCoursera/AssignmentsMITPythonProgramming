d1 = {}
d2 = {}

def f(a, b):
    return a>b
    
def dict_interdiff(d1, d2):
    a = {}
    b = {}
    c = ()
    if(d1=={} or d2 =={}):
        c =(d1,d2)
        return c
    else:
        for i in range(0,max(max(dict.keys(d1)),max(dict.keys(d2)))+1):
            if((i in dict.keys(d1)) and (i in dict.keys(d2))):
                a[i] = f(d1[i], d2[i])
            else:
                if(i in dict.keys(d1)):
                    b[i] = d1[i]
                elif(i in dict.keys(d2)):
                    b[i] = d2[i]
                else:
                    continue
        c = (a,b)
        return c
    
