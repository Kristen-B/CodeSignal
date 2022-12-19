def solution(picture):
    
    inside_width=len(picture[0])
    inside_height=len(picture)
    
    outside_height=inside_height+2
    outside_width=inside_width+2
    
    total=[]
    s=[]
    line=[]
    
    
    for i in range(0,outside_height):
        
        line=[]
        
        for j in range(0,outside_width):
            
            if (i==0 or i==outside_height-1 or j==0 or j==outside_width-1):
                line.append('*')
                
            else:
                #return len(picture), inside_width
                line.append(picture[i-1][j-1])
                
        word = ''.join(line)
        total.append(word)
        
        
                
    result_4 = total[0].split()
    
    return total
