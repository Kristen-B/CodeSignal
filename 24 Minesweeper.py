def solution(matrix):
    
    matrixcopy = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))] 
    
    for i in range(0,len(matrix)):
        for j in range(0, len(matrix[0])):
            if(matrix[i][j]==True):
                matrixcopy=add1(matrixcopy,i,j)
                print('')
                
    return matrixcopy
                
                
def add1(matrix,i,j):
    if(j==len(matrix[0])-1):
        print(j,i,len(matrix[0])-1)
        print(matrix[i][j],j>0 and i<len(matrix)-1)
    if(i<len(matrix)-1):
        matrix[i+1][j]+=1
        print (matrix)
    if(0<i):
        matrix[i-1][j]+=1
        print (matrix)
    if(0<j):
        matrix[i][j-1]+=1
        print (matrix)
    if(j<len(matrix)-1):
        matrix[i][j+1]+=1
        print (matrix)
    if(j<len(matrix)-1 and i<len(matrix)-1):
        matrix[i+1][j+1]+=1
        print (matrix)
    if(j>0 and i<len(matrix)-1):
        matrix[i+1][j-1]+=1
        print (matrix)
    if(j>0 and i>0):
        matrix[i-1][j-1]+=1
        print (matrix)
    if(j<len(matrix)-1 and i>0):
        matrix[i-1][j+1]+=1 
        print (matrix)
        
    return matrix   
    
