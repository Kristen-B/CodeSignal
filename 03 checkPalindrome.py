#Checks for palindrome

def solution(inputString):
    
    #Assume solution (sol) is true
    sol=True
    
    #Compare first half w last half    
    for i in range(0,int(len(inputString)/2)):
        
        #Checks if start of string matches end of string
        if(inputString[i]==inputString[len(inputString)-1-i]):
            pass
            
        #If not returns False
        else:
            return False
            
    return sol
