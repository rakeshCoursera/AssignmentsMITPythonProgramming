def oddTuples(aTup):
    oddT=()
    print type(oddT)
    print len(aTup)
    for i in range(0,len(aTup)):
        print i
        if(i%2==1):
            oddT = oddT +(aTup[i],)
    return oddT
