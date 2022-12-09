def solve( A):
    flag1=0
    flag2=0
    even_first=0
    odd_first=0
    for i in range (len(A)):
        if A[i]%2==0 and flag1==0:
            even_first+=1
            flag1=1
        elif A[i]%2==1 and flag1==1:
            even_first+=1
            flag1=0
        
        if A[i]%2==1 and flag2==0:
            odd_first+=1
            flag2=1
        elif A[i]%2==0 and flag2==1:
            odd_first+=1
            flag2=0
        
    
    return max(even_first,odd_first)

A=[ 16, 50, 2, 9, 40, 2, 19, 43, 14 ]
print(solve(A))
