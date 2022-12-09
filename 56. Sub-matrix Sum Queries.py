from sys import prefix


def solve(A, B, C, D, E):
    prefix_sum= A.copy()
        
    for i in range(0,len(A)):
        prefix_sum[i][0]=A[i][0]%(pow(10,9)+7)
        for j in range(1,len(A[0])):
            prefix_sum[i][j]=prefix_sum[i][j-1]%(pow(10,9)+7)+A[i][j]%(pow(10,9)+7)
    
    for j in range(0,len(A[0])):
        for i in range(1,len(A)):
            prefix_sum[i][j]=prefix_sum[i-1][j]%(pow(10,9)+7)+prefix_sum[i][j]%(pow(10,9)+7)
    
    print(prefix_sum)
    result=[]
    for i in range(len(B)):
        """
        left=1
        top=1
        if B[i]==1:
            top=0
        if C[i]==1:
            left=0
        
        sub_sum=prefix_sum[D[i]-1][E[i]-1]+prefix_sum[B[i]-2][C[i]-2]*top*left-prefix_sum[D[i]-1][C[i]-2]*left-prefix_sum[B[i]-2][E[i]-1]*top 
        """
        sub_sum=prefix_sum[D[i]-1][E[i]-1]
        print(1,sub_sum)
        if B[i]>1:
            sub_sum-=prefix_sum[B[i]-2][E[i]-1]
            print(2,sub_sum)
        if C[i]>1:
            sub_sum-=prefix_sum[D[i]-1][C[i]-2]
            print(3,sub_sum)
        if C[i]>1 and B[i]>1:
            sub_sum+=prefix_sum[B[i]-2][C[i]-2]
            print(4,sub_sum)
        result.append(sub_sum)
    return result

A=[
  [5, 7, 100, 11],
  [0, 0, 2, 8]
]
B,C,D,E=[1,1],[1,4],[2,2],[2,4]
print(solve(A,B,C,D,E))

