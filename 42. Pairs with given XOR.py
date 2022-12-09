    
def solve(A,B):
    xor=[0]*len(A)
    xor[0]=A[0]
    data={A[0]:1}
    for i in range(1,len(A)):
        xor[i]=xor[i-1]^A[i]^B
        if xor[i] in data:
            data[xor[i]]+=1
        else:
            data[xor[i]]=1
    print(xor)
    print (data)
    count=0
    for v in data:
        if data[v]>1:
            count+=1
        if v==B:
            count+=data[v]
    return count
A=[ 17, 18, 8, 13, 15, 7, 11, 5, 4, 9, 12, 6, 10, 14, 16, 3 ]
B=9
print(solve(A,B))