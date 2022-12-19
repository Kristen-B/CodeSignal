def solution(a, b):
    
    same = True
    error=0
    incorrect_i = []
    
    #compare a and b~ if 1 is not right
    for i in range(0,len(a)):
        
        if(a[i]==b[i]):
            pass
            
        else:
            same=False
            error=error+1
            incorrect_i.append(i)
    
    if (error/2 ==1):
        
        if (a[incorrect_i[0]]==b[incorrect_i[1]] and a[incorrect_i[1]]==b[incorrect_i[0]] ):
            return True
            
        else:
            return False
            
    elif(error==0):
        return True
        
    else:
        return False
