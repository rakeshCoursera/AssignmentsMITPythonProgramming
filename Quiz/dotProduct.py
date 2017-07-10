listA = [1, 2, 3]
listB = [4, 5, 6]
def dotProduct(listA, listB):
    total =0
    for i in range(len(listA)):
        total = total + listA[i]*listB[i]
    return total
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
