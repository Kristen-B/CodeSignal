# returns the century
def solution(year):
    
    century=1
    count=1
    
    for i in range(1,year):
        
        count=count+1
        
        if(count==101):
            
            count=1
            century=century+1
            
    return century
