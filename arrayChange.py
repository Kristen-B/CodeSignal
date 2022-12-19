def solution(inputArray):
    
    counter=0
    
    for i in range(0, len(inputArray)-1):
        
        while(inputArray[i]>=inputArray[i+1] and inputArray[i]<=10**5 ):
            
            if(inputArray[i]-inputArray[i+1]>100):
                #return inputArray
                inputArray[i+1]+=100
                counter+=100
                
            else:
                #return inputArray
                inputArray[i+1]+=1
                counter+=1
       
        
    return counter

