def solution(a):
    
    i=0
    while (i<len(a)):
        
        if(a[i]==-1):
            i=i+1
            
        else:
            maxa=a[i]
            
            for j in range(i,len(a)):
                
                if(a[j]<maxa and a[j]!=-1):
                    maxa=a[j]
                    a[j]=a[i]
                    a[i]=maxa 
                    
            i=i+1
            
    return a
            
            
