def solution(s1, s2):
    
    num=0
    s1copy=sorted(s1)
    s2copy=sorted(s2)
    
    #see s1[i] compare to s2[j], if any match then add 1 only
    for i in range(0,len(s1copy)):
        
        add=False
        
        for j in range(0,len(s2copy)):
            
            if(s1copy[i]==s2copy[j] ):
                add=True
                s2copy[j]=0
                break
            
        if(add==True):
            num=num+1
            
    return num

