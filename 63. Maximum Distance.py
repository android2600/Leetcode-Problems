def maximumGap(A):
    #Brute
    """
    max_distance=[0]*len(A)
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[j]>=A[i]:
                max_distance[i]=max(max_distance[i],j)
    return max(max_distance)
    """    
    prefix_max=[0]*len(A)
    prefix_max[0]=A[0]
    prefix_min=[0]*len(A)
    prefix_min[0]=A[0]
        
    for i in range(1,len(A)):
        prefix_min[i]=min(prefix_min[i-1],A[i])    
        prefix_max[i]=max(prefix_max[i-1],A[i])
    i=0
    j=0
    result=-1
    print(prefix_max,prefix_min)
    while j<len(A) and i<len(A):
        if prefix_max[i]>prefix_min[j]:
            i+=1
        elif prefix_max[i]<=prefix_min[j]:
            j+=1
        result=max(j-i,result)
    return result-1

A=[1,10]
#A=[-1,-1,2]
#A=[3,2,1]
print(maximumGap(A))