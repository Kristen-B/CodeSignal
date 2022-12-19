def solution(inputArray):
    
    maxdiff = 0
    
    for i in range(0,len(inputArray)-1):
        
        diff=inputArray[i]-inputArray[i+1]
        
        if (abs(diff)>maxdiff):
            maxdiff = abs(diff)
            
    return maxdiff

