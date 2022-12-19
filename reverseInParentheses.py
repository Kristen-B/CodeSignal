def solution(inputString):
    
    i=0
    segment=[]
    segment=list(inputString)
    
    #return segment
    while (i<len(segment)):
        
        #find first )
        a=i
        
        if(segment[i]==')'):
            
            while (segment[i]!='('):
                i=i-1
                
            b=i
            segment.pop(a)
            segment.pop(b)
            
            #return segment
            rev=segment[b:a-1]
            rev=reverse(rev,segment,b)
            segment[b:a-1]=rev
            a=a-2
            
            
        i=a+1
        
    if(len("".join(segment))>0): 
        return "".join(segment)
        
    else:
        return ""
    
def reverse(r_segment,total,initial):
    
    if(len(r_segment)<len(total)):
        
        for i in range(0,len(r_segment)):
            r_segment[i]=total[len(r_segment)-i+initial-1]
            
        return r_segment
            
    else:
        
        for i in range(0,len(r_segment)):
            r_segment[i]=total[len(r_segment)-i-1]
            
        return r_segment
        
        
