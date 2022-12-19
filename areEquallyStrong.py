def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    
    your=[yourLeft,yourRight]
    friend=[friendsLeft, friendsRight]
    
    if(max(your)==max(friend)):
        pass
        
    else:
        return False
        
    if(min(your)==min(friend)):
        return True
        
    else:
        return False
