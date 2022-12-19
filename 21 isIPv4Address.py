def solution(inputString):
    
    address = inputString.split(".")
    
    if(len(address)!=4):
        return False
        
    print(address)
        
    for i in range(0,len(address)):
        
        if(address[i]=="" or address[i].isdigit()==False):
            return False
            
        elif(int(address[i])>255):
            return False
            
        elif(int(address[i][0])==0 and len(address[i][:])>1):
            return False
            
    return True

