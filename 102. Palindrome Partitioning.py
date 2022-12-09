def solve(A):
    palin=[[0 for j in range(len(A)+1)] for i in range(len(A)+1)]
    for i in range(len(A)):
        palin[i][i]=1
    for letters in range(2,len(A)+1):
        for i in range(1,len(A)+2-letters):
            j=i+letters-1
            if letters==2:
                if A[i-1]==A[j-1]:
                    palin[i][j]=1
            else:
                if A[i-1]==A[j-1] and palin[i+1][j-1]==1:
                    palin[i][j]= 1
    dp=[len(A) for i in range(len(A)+1)]
    for i in range(2,len(A)+1):
        if palin[1][i]==1:
            dp[i]=0
        for j in range(2,i+1):
            if palin[j][i]==1:
                dp[i]=min(dp[i],1+dp[j-1])
    print(*palin)
    print(dp[-2])
    print(dp)

solve("aabasda")       