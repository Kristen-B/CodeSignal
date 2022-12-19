def solution(image):
    
    ans=[]
       
    #image is at min length 3x3
    for i in range(0,len(image)-2):
        ans.append(threexthree(image,i))
        
    return ans
    
    
def threexthree(image,indexI):
    
    ans=[]
    avg_sum=0
    j_step=0
    
    while j_step<len(image[0])-2:
        
        for i in range(indexI,indexI+3):
            
            for j in range(j_step,j_step+3):
                
                avg_sum=avg_sum+image[i][j]
                
        j_step=j_step+1
        ans.append(int(avg_sum/9))
        avg_sum=0
          
            
    return ans
        
