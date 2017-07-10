def semordnilap(str1, str2):
    len1=len(str1)
    len2=len(str2)
    if(len(str1) != len(str2)):
       return False
    elif(str1=='' and str2==''):
       return True
    else:
       if (str1[0]==str2[-1]):
           return semordnilap(str1[1:], str2[:-1])

    
def semordnilapWrapper(str1, str2):
    if len(str1) == 1 or len(str2) == 1:
        return False
    
    if str1 == str2:
        return False

    return semordnilap(str1, str2)
