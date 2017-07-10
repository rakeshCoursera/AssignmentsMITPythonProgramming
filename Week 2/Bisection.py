# lecture 3.6, slide 2
# bisection search for square root

#x = input("Enter a secret Number between 0 to 100: ")
x=42
l = 0
h = 100
numGuesses = 1
c = (h + l)/2.0
while c != x:
    print('low value = ' + str(l) + ' high value = ' + str(h) + ' Center Value = ' + str(c))
    numGuesses += 1
    print c,x;
    print(type(c),' ',type(x) )
    if(c>x):
        h=c
    else:
        l=c
    c = round((h + l)/2.0)
print('numGuesses = ' + str(numGuesses))
print(str(c) + ' is the entered secret value ')
