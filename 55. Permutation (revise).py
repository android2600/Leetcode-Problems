class Solution:
    def __init__(self):
        self.result=[]
    def solve(self,A):
        def permute(A,l,r):
            if l==r:
                self.result.append(A.copy())
                return
            for i in range(l,r):
                A[i],A[l]=A[l],A[i]
                permute(A,l+1,r)
                A[l],A[i]=A[i],A[l]
        permute(A,0,len(A))
        return self.result

A=[1,2,3]
res_=Solution()
print(res_.solve(A))