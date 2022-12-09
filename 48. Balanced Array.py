def solve(A):
    if len(A)==1:
        return 1
    elif len(A)==2:
        return 0

    A_even=[0]*len(A)
    A_odd=[0]*len(A)
    A_even[0]=A[0]
    A_odd[1]=A[1]
    for i in range(1,len(A)):
        if i%2==0:
            A_even[i]=A_even[i-1]+A[i]
            A_odd[i]=A_odd[i-1]
        else:
            A_odd[i]=A_odd[i-1]+A[i]
            A_even[i]=A_even[i-1]
    #print(A_even,A_odd)
    count=0
    for i in range(0,len(A)):        
        if i>0:
            if (A_even[len(A)-1]-A_even[i]+A_odd[i-1])==(A_odd[len(A)-1]-A_odd[i]+A_even[i-1]):
                count+=1
        else:
            if (A_even[len(A)-1]-A_even[i])==(A_odd[len(A)-1]-A_odd[i]):
                count+=1
    return count
A=[5, 5, 2, 5, 8]
print(solve(A))
