def solution(sequence):
    
    copy1=sequence.copy()
    copy2=sequence.copy()
    invalid=0
    index=0
    
    for i in range(1,len(sequence)):
        
        if(sequence[i-1]<sequence[i]):
            pass
            
        else:
            invalid=invalid+1
            index=i
            
            
    if (invalid>1):
        return False
        
    elif(invalid>0):
        
        copy1.pop(index-1)
        copy2.pop(index)
        #check
        invalid =0
        
        for i in range(0,len(copy1)-1):
            
            if(copy1[i]<copy1[i+1]):
                pass
                
            else:
                invalid=1
                
                
            if(copy2[i]<copy2[i+1]):
                pass
        
            else:
                invalid=invalid+1
               
                
        if (invalid>1):
            return False
            
        else:
            return True
            
    else:
        return True
            
