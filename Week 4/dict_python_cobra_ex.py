Dict = {'A': 4, 'B': 1, 'C': 2}
ptn = 'BC'
def nfruits(Dict,ptn):
    L = len(ptn)
    m=0
    Max_fruit=0
    while(min(dict.values(Dict))>0):
        print "Enter in while loop"
        for i in range(L):
            print "Enter in for loop"
            if(Dict[ptn[m]]==0):
                Dict[ptn[i]] -= 1
                Max_fruit = max(dict.values(Dict))
                print Max_fruit
                print Dict
            else:
                Dict[ptn[i]] -= 1
                print Dict
                for k in dict.keys(Dict):
                     if(k != ptn[i]):
                         Dict[k] += 1
                         print "Dict-:",Dict
            m=i
    return Max_fruit

                         
                         
            
                
                
        
    
    
