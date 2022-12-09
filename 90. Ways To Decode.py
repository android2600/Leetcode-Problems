class Solution:
	# @param A : string
	# @return an integer
    def numDecodings(self, A):
        m=1000000007
        if len(A)==1:
            return 1
        
        dp=[0]*len(A)
        dp[0]=1
        if int(A[1])!=0 and int(A[0:2])<=26:
            dp[1]=2
        else:
            dp[1]=1

        for i in range(2,len(A)):
            if int(A[i-1:i+1])>10 and int(A[i-1:i+1])<=26:
                dp[i]=(dp[i-1]+dp[i-2])%m
            else:
                dp[i]=dp[i-1]
        return dp[-1]%m

obj=Solution()
A="2611055971756562"
print(obj.numDecodings(A))
