def solution(inputArray):
    
    sortInputArray=sorted(inputArray)
    Jump=1
    JumpTotal=0
    
    while (JumpTotal<max(inputArray)):
        
        JumpTotal=JumpTotal+Jump
        print(JumpTotal,Jump)
        
        if JumpTotal in inputArray:
            JumpTotal=0
            Jump+=1
    
    return Jump
