def solution(statues):
    
    mod_stat=sorted(statues)
    i_stat=mod_stat[0]
    num=0
    
    for i in range(1,len(statues)):
        
        for j in range(0,20):
            
            if(mod_stat[i]!=i_stat+1):
                
                num=num+1
                i_stat=i_stat+1
                
            else:
                
                j=20
                
        i_stat=i_stat+1
        
    return num
                
