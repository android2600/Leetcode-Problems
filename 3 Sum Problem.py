def threeSum(A):
    if len(A)<3:
        return []
    A.sort()
    result=[]
    i=0
    while i<len(A)-1:
        j,k=i+1,len(A)-1
        while j<k and A[j]==A[j+1]:
            j+=1
        while j<k and A[k]==A[k-1]:
            k-=1
        while j<k:
            if -A[i]<A[j]+A[k]:
                k-=1
            elif -A[i]>A[j]+A[k]:
                j+=1
            else:
                result.append([A[i],A[j],A[k]])
                j+=1
                k-=1
        i+=1
    return result

A=[ 1, -4, 0, 0, 5, -5, 1, 0, -2, 4, -4, 1, -1, -4, 3, 4, -1, -1, -3 ]
print(threeSum(A))