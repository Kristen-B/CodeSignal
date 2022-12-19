def solution(matrix):
    
    no_col = int(len(matrix[0]))
    no_row = int(len(matrix))
    tot=0
    ghost_pos=[]
    ghost =False
    
    #will not add at [i,j], [col,row] if at matrix[col,row+1] has ghosts
    
    for i in range(0,no_row):
        
        for j in range(0,no_col):
            
            if (i==0):
                tot=tot+matrix[i][j]
                
            else:
                ghost=False
                
                for k in range(0,i):
                    
                    if(matrix[k][j]==0):
                        ghost=True
                        
                
                if (ghost==False):
                    tot=tot+matrix[i][j]
                
            
                    
    
    return tot
