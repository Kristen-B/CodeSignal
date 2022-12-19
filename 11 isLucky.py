def solution(n):
    
    st_n=res = list(map(int, str(n)))
    size_n=len(st_n)
    
    f_half=st_n[0:int(size_n/2)]
    l_half=st_n[int(size_n/2):size_n]
    
    #return sum(f_half),l_half
    if(sum(f_half)==sum(l_half)):
        return True
        
    else:
        return False
