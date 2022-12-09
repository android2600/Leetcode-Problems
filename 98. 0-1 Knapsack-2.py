def solve(A, B, C):
    N=len(A)
    total=sum(A)
    dp=[[[0,0] for i in range(total+1)] for j in range(N+1)]
    max_val=0
    for i in range(1,N+1):
        for j in range(1,total+1):
            if j>=A[i-1] and dp[i-1][j-A[i-1]][0]+B[i-1]<=C and dp[i-1][j][0]>=dp[i-1][j-A[i-1]][0]+B[i-1]:
                dp[i][j]=[dp[i-1][j-A[i-1]][0]+B[i-1],dp[i-1][j-A[i-1]][1]+A[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
            max_val=max(max_val,dp[i][j][1])
    return max_val
A = [ 9, 3, 5, 6, 6, 2, 8, 2, 2, 6, 3, 8, 7, 2, 5, 3, 4, 3, 3 ]
B = [ 22, 17, 19, 46, 48, 27, 22, 39, 20, 13, 18, 50, 36, 45, 4, 12, 23, 34, 24 ]
C = 513
print(solve(A,B,C))