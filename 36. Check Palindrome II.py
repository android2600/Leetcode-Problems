def solve( A):
    data={}
    for i in range(len(A)):
        if A[i] in data:
            data[A[i]]+=1
        else:
            data[A[i]]=1
    
    print(data,len(A))
    flag=0
    for v in data:
        if(len(A)%2==0 and data[v]%2==0):
            pass
        elif(len(A)%2==1 and data[v]%2==0 and flag<2):
            pass
        elif(len(A)%2==1 and data[v]%2==1 and flag<1):
            flag+=1
        else:
            return 0
    return 1
A="vnpypznzpfxyivpppxfpp"
print(solve(A))
    