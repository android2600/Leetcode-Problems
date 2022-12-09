class Trie:
    def __init__(self):
        self.node = [None,None]

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def max_xor_subarray(self,curr,a,m):
        ans = 0
        for i in range(m,-1,-1):
            bit = (a>>i)&1
            if curr.node[1-bit]:
                ans += 1<<i
                curr = curr.node[1-bit]
            else:
                curr = curr.node[bit]
        return ans

    def msb(self,n):
        ans = 0
        while(n>0):
            n = n>>1
            ans += 1
        return ans

    def insert(self,curr,a,m):
        for i in range(m,-1,-1): #Important step
            bit = (a>>i)&1
            if not curr.node[bit]:
                curr.node[bit] = Trie()
            curr = curr.node[bit]

    def solve(self, A):
        pfxor = [None]*(len(A)+1)
        pfxor[0] = 0
        for i in range(1,len(A)+1):
            pfxor[i] = pfxor[i-1]^A[i-1]
        r = Trie()
        n = max(pfxor)
        m = self.msb(n)
        #return [m]
        for i in range(len(pfxor)):
            curr = r
            self.insert(curr,pfxor[i],m)
        
        ans = 0
        for j in range(len(pfxor)):
            curr_ans = 0
            a = pfxor[j]
            curr = r
            ans = max(ans,self.max_xor_subarray(curr,a,m))
        
        # ans has max xor value of the subarray from cummulative xor array

        min_len = float('inf')
        min_start = float('inf')
        min_end = float('inf')
        idx = {}
        for i in range(len(pfxor)): 
            val = ans^pfxor[i]
            if(val in idx):
                start = idx[val] + 1
                end = i
                length = end-start+1
                if(length<min_len):
                    min_len = length
                    min_start = start
                    min_end = end
                elif(length==min_len and start<min_start):
                    min_start = start
                    min_end = end
            idx[pfxor[i]] = i
        return [min_start,min_end]

A = [ 33, 29, 18 ]
A=[15,25,23]
A=[ 19, 17, 7, 7, 23 ]
obj=Solution()
print(obj.solve(A))
