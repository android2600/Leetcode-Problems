class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    """
    def check_bit(self,num,index):
        if num & 1<<index==0:
            return False
        else:
            return True

    def subsets(self, A):
        result=[]
        result.append([])
        for i in range(1,1<<len(A)):
            result_sub=[]
            for j in range(len(A)):
                if self.check_bit(i,j):    
                    result_sub.append(A[j])
            result.append(result_sub)
        
        return result
    """
    def __init__(self):
        self.result = []

    def subsets(self,A):
        A.sort()
        temp=[]
        self.computeSubSet(0, A, temp)
        return self.result

    def computeSubSet(self, index, A, tempList):
        new=[x for x in tempList]
        self.result.append(new)
        for i in range(index,len(A)):
            tempList.append(A[i])
            self.computeSubSet(i+1, A, tempList)
            tempList.pop()

A=[12,13,14]
run_=Solution()
print(run_.subsets(A))