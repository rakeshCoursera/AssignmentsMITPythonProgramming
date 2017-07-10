A = 56569
B = 125
def solution(A,B):
    a = str(A)
    b = str(B)
    c = ''
    for i in range(min(len(a),len(b))):
        c = c + a[i]
        c = c + b[i]
        j = i
    c = c + a[j+1:]
    c = c + b[j+1:]
    if(int(c)>100000000):
        return -1
    else:
        return int(c)

        
        
