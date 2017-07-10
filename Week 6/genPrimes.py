def genPrimes():
    n=2
    Primes =[n]
    while True:
        signal =0
        n = n+1
        #print Primes
        for p in Primes:
            #print p,n
            if(n%p == 0):
                signal = 1
                break
        #print "Signal",signal
        if(signal ==0):
            #print n
            Primes.append(n)
            yield n
