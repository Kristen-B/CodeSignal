def solution(inputArray):    
    
    maxlen=0
    maxarr=[]
    
    for i in range(0,len(inputArray)):
        
        if(len(inputArray[i])>maxlen):
            maxlen=len(inputArray[i])
            
    for i in range(0,len(inputArray)):
        
        if(len(inputArray[i])==maxlen):
            maxarr.append(inputArray[i])
            
    return maxarr
