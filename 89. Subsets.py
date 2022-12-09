class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    def __init__(self):
        self.result=[]
    
    def backtrack(self,A,n,index,array):
        arr=array.copy()
        self.result.append(arr)
        for j in range(index,n):
            arr.append(A[j])
            self.backtrack(A,n,index+1,arr)
            arr.pop()     

    def subsets(self, A):
        A.sort()
        arr=[]
        self.backtrack(A,len(A),0,arr)
        return self.result

obj=Solution()
print(obj.subsets([1,2,3]))
