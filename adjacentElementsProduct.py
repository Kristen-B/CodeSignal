def solution(inputArray):
    
    maxval = inputArray[0]*inputArray[1]
    
    for i in range(1,len(inputArray)-1):
        
        if(inputArray[i]*inputArray[i+1]>maxval):
            
            maxval = inputArray[i]*inputArray[i+1]
            
    return maxval

