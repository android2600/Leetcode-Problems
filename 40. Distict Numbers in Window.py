def dNums(A, B):
    data={}
    result=[]
    for i in range(B):
        if A[i] in data:
            data[A[i]]+=1
        else:
            data[A[i]]=1
    
    result.append(len(data))
    
    for i in range(B,len(A)):
        if A[i] in data:
            data[A[i]]+=1
        else:
            data[A[i]]=1

        if data[A[i-B]]>=1:
            data[A[i-B]]-=1
        
        if data[A[i-B]]==0:
            del data[A[i-B]]
            
        result.append(len(data))
    
    return result

A=[ 1, 2, 1, 3, 4, 3 ]
B=3
print(dNums(A,B))
