def isInterleave(A, B, C):
    dp=[["0" for j in range(len(B)+1)] for i in range(len(A)+1)]
    for i in range(len(A)+1):
        for j in range(len(B)+1):
            if i==0 and j==0:
                dp[i][j]="1"
            elif i==0 and C[i+j-1]==B[j-1]:
                dp[i][j]=dp[i][j-1]
            elif j==0 and C[i+j-1]==A[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                if C[i+j-1]==A[i-1] and dp[i-1][j]=="1":
                    dp[i][j]=dp[i-1][j]
                elif C[i+j-1]==B[j-1] and dp[i][j-1]=="1":
                    dp[i][j]=dp[i][j-1]
    print(*["".join(dp[i]) for i in range(len(dp))])
    return dp[-1][-1]

#A = "noUdRp97xFvpifeSXGwOjcVNhHo9N2D"
#B = "6iZItw9A3fj86uYx04tvWKLtl9BK"
#C = "n6ioUdRpZ97ItwxF9Av3fj86upYxif0eS4XtvWKLtlG9wOBKjcVNhHo9N2D"
A = "eZCHXr0CgsB4O3TCDlitYI7kH38rEElI"
B = "UhSQsB6CWAHE6zzphz5B"
C = "eUZCHhXr0SQsCgsB4O3B6TCWCDlAitYIHE7k6H3z8zrphz5EEBlI"

A = "accbaabaaabbcbaacbababacaababbcbabaababcaabbbbbcacbaa"
B = "cabaabcbabcbaaaacababccbbccaaabaacbbaaabccacabaaccbbcbcb"
C = "accbcaaabbaabaaabbcbcbabacbacbababaacaaaaacbabaabbcbccbbabbccaaaaabaabcabbcaabaaabbcbcbbbcacabaaacccbbcbbaacb"
A = "LgR8D8k7t8KIprKDTQ7aoo7ed6mhKQwWlFxXpyjPkh"
B = "Q7wQk8rqjaH971SqSQJAMgqYyETo4KmlF4ybf"
C = "Q7wLgR8D8Qkk7t88KIrpqjarHKD971SqSQJTQ7aoAMgoq7eYd6yETmhoK4KmlQwWFlF4xybXfpyjPkh"

print(isInterleave(A,B,C))