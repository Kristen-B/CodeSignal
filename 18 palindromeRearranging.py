def solution(inputString):
    
    # sort list; aabbcc
    # when input string is even if each letter has a pair then it's a palendrom
    # abccba
    # when input string is odd, allowed to have 1 and 1 only remaining left over
    # check by comparing in 2's, when not matching, move only by 1 and proceed by 2's
    
    no=0
    sortedString=sorted(list(inputString))
    
    if(len(sortedString)%2==0):
        
        for i in range(0,int(len(sortedString)/2)):
            
            if(sortedString[i*2]==sortedString[i*2+1]):
                pass
                
            else:
                return False
                
        return True
        
    elif(len(sortedString)==1):
        return True
        
    elif(len(sortedString)==3):
        i=0
        
        while (i <int(len(sortedString)/2+1)):
            
            if(sortedString[i]==sortedString[i+1]):
                i+=2
                pass
                
            else:
                return False
                
        return True
        
    else:
        
        i=0
        
        while (i <int(len(sortedString)/2+2)):
            
            if(sortedString[i]==sortedString[i+1]):
                i+=2
                pass
                
            else:
                
                if(no==1):
                    return False
                
                no=1
                i+=1
                
                if(len(sortedString)==3):
                    return True
       
        
        return True
