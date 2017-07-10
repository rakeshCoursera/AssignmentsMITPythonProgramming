A = [3, 5, 6, 3, 3, 5]
print A

def solution(A):
    n =0
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if(A[i]==A[j]):
                n = n+1
                print "Identical Pair (", i,",",j,")"
    return n
                
