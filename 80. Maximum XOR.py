class Node:
    def __init__(self):
        self.val=[None,None]

class Solution:
    # @param A : list of integers
    # @return an integer
    def __init__(self):
        self.root=Node()

    def bits(self,A):
        count=0
        while A>0:
            A=A>>1
            count+=1
        return count
    
    def insert(self,A,max_bits):
        h=self.root
        for i in range(max_bits-1,-1,-1):
            bit= A>>i&1
            if not h.val[bit]:
                h.val[bit]=Node()
                h=h.val[bit]
            else:
                h=h.val[bit]
    
    def query(self,A,max_bits):
        h=self.root
        result=0
        if A==17:
            print("")
        for i in range(max_bits-1,-1,-1):
            bit= A>>i&1
            if h.val[1-bit]:
                h=h.val[1-bit]
                result+= 1<<i
            elif h.val[bit]:
                h=h.val[bit]
        return result

    def solve(self, A):
        max_val=max(A)
        max_bits=self.bits(max_val)
        
        for i in range(len(A)):
            self.insert(A[i],max_bits)
        
        result=0
        for i in range(len(A)):
            result=max(result,self.query(A[i],max_bits))
        return result
    
    def check(self,A):
        result=0
        num1,num2=0,0
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                if result<A[i]^A[j]:
                    result=A[i]^A[j]
                    num1=A[i]
                    num2=A[j]
        return result,num1,num2

A=[4,7,9,15,17,21]
obj=Solution()
print(obj.solve(A))
print(obj.check(A))