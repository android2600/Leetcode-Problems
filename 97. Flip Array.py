class Solution:
	# @param A : tuple of integers
	# @return an integer
    def solve(self, A):# Knapsack problem
        N = len(A)
        sum_ = 0
        for i in range (N):
            sum_ += A[i]

        halfsum = sum_ // 2
        dp=[[float("inf") for i in range(halfsum+1)] for j in range(N+1)]
        for i in range(N+1):
            dp[i][0]=0
        
        for i in range(1,N+1):
            for j in range(1,halfsum+1):
                if j >= A[i-1]:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j - A[i-1]] + 1)
                else:
                    dp[i][j] = dp[i-1][j]

        while halfsum >0 and dp[N][halfsum]==float("inf"):
            halfsum-=1
        
        return dp[N][halfsum]

A=[9,6]
obj=Solution()
print(obj.solve(A))