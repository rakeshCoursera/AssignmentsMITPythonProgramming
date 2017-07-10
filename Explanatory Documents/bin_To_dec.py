def binary(n):
   """Function to print binary number
   for the input decimal using recursion"""
   if n > 1:
       return (str(binary(n//2))+str(n%2))
   return 1  
       
    

# Take decimal number from user
x=''
dec = int(input("Enter an integer: "))
x=bin(dec)
'''x =str(binary(dec))'''
print x[1]
#print(type(x))
z=[]
count = 0
for i in range(len(x)):
    #print x[i]
    if(x[i]=='1'):
        count = count+1
    else:
        #print count
        z.append(count)
        count =0
    z.append(count)
print max(z)
        




