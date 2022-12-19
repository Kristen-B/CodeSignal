def solution(a):
    
    a1=0
    a2=0
    
    for i in range(0,len(a)):
        
        if(i%2==0):
            a1=a1+a[i]
            
        else:
            a2=a2+a[i]
            
    b=[a1,a2]
    
    return b
