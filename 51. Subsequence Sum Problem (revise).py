class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def check_bit(self,num,index):
        if num & 1<<index==0:
            return False
        else:
            return True

    def solve1(self, A, B):
        
        for i in range(1,1<<len(A)):
            sum_=0
            for j in range(len(A)):
                if self.check_bit(i,j):
                    sum_+=A[j]
                if sum_==B:
                    return 1
        
        return 0
    
    def solve2(self,A,B):

        def isSubsetSum(set, n, sum):

            # Base Cases
            if (sum == 0):
                return True
            if (n == 0):
                return False
        
            # If last element is greater than
            # sum, then ignore it
            if (set[n - 1] > sum):
                return isSubsetSum(set, n - 1, sum)
        
            # else, check if sum can be obtained
            # by any of the following
            # (a) including the last element
            # (b) excluding the last element
            return isSubsetSum(
                set, n-1, sum) or isSubsetSum(
                set, n-1, sum-set[n-1])
        
        if isSubsetSum(A,len(A),B)== False:
            return 0
        else:
            return 1

run_=Solution()
x=run_.solve2([ 76, 55, 23, 66, 7, 52, 21, 2, 21, 42 ],72)
print(x)