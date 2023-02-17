def solution(matrix):
    
    print(matrix[0][:])
    print(matrix[:][0]) 
    print(matrix)  
    
    matrixcopy = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))] 
   
        
    
    for i in range(0,len(matrix)):
        for j in range(0, len(matrix[0])):
            
            if(matrix[i][j]==True):
                matrixcopy=add1(matrixcopy,i,j)
    print(matrixcopy[0])
    print(matrixcopy[1][0]) 
    print(matrixcopy)  
   
    return matrixcopy
                
def add1(matrixcopy,i,j):
    # where i and j are the indices of the 'mine' on the board
    '''
    3 types for corner
    5 types for edge
    8 types for centre
    
    corner if indices are combination of strictly 0 and len()
    edge if indices are either 0 or len() but not doubles
    centre when neither are 0 or len()
    
    note; when at 0 add don't take, when at len() take don't add
    '''
    
# top rows (not bottom) ~ adds to values underneath   
    if(i==0 or i<len(matrixcopy)-1):
        # value down
        matrixcopy[i+1][j]+=1
        
        # adds to starting collumns (not end)
        if(j==0 or j<len(matrixcopy[0])-1):
            #value right
            matrixcopy[i][j+1]+=1
            #value right and down
            matrixcopy[i+1][j+1]+=1
            
        if(j==len(matrixcopy[0])-1 or j>0):
            #value left
            matrixcopy[i][j-1]+=1
            #value left and down
            matrixcopy[i+1][j-1]+=1
            
            
    if(i==len(matrixcopy)-1 or i>0):
        #value down
        matrixcopy[i-1][j]+=1
        
        if(j==0 or j<len(matrixcopy[0])-1):
            #value down and right
            matrixcopy[i-1][j+1]+=1
            #value right if not already added (i.e. bottom edge)
            if(i==len(matrixcopy)-1):
                matrixcopy[i][j+1]+=1
            
            
        if(j==len(matrixcopy[0])-1 or j>0):
            #value down and left
            matrixcopy[i-1][j-1]+=1
            if(i==len(matrixcopy)-1):
                matrixcopy[i][j-1]+=1
            
    return matrixcopy
            
            
            
        
    
        

