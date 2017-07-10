#S = "13+62*7+*"
S = "11++"
def solution(S):
    n = len(S)
    stack = []
    j=0
    for i in range(n):
        if(S[i] == "+"):
            #print j
            if(j<=1):
                #print "invalid string, can pop"
                return -1
            else:
                stack[j-2]= stack[j-2]+stack[j-1]
                del(stack[j-1])
                j -= 1
                #print "+ operators",stack
        elif(S[i] =="*"):
            if(j<=1):
                #print "invalid string, can pop"
                return -1
            else:
                stack[j-2]= stack[j-2]*stack[j-1]
                del(stack[j-1])
                j -= 1
                #print "* operators",stack
        else:
            stack.append(int(S[i]))
            j += 1
            #print "simple number",stack
    return stack
        
    
