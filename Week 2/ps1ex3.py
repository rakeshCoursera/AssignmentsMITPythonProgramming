s = 'azcbobobegghakl'
#count = s.count('bob')
count = 0
for x in range(len(s)-2):
               print (s[x]+s[x+1]+s[x+2])
               if(s[x]+s[x+1]+s[x+2]=='bob'):
                  count += 1
print ("Number of times bob occurs is: " +str(count))
    
