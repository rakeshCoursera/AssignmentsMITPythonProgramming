aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(aList):
    if(aList ==[]):
        return []
    else:
        if((type(aList))==list):
            a = flatten(aList[0])
            #print a
            b = flatten(aList[1:])
            #print b
            a.extend(b)
            return a
        else:
            return [aList]
'''
def flatten(aList):
    if(aList==[]): 
        return []
    elif(type(aList) != list): 
        return [aList]
    else:
        a = flatten(aList[0])
        #print a
        b = flatten(aList[1:])
        #print b
        a.extend(b)
        return a
''' 
  
