class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
    def heapify(self,A,index):
        child1=2*index+1
        child2=2*index+2
        smaller=index
        if child1<len(A) and A[smaller][0]+A[smaller][1]>A[child1][0]+A[child1][1]:
            smaller=child1
        if child2<len(A) and A[smaller][0]+A[smaller][1]>A[child2][0]+A[child2][1]:
            smaller=child2
        if index!=smaller:
            A[index],A[smaller]=A[smaller],A[index]
            self.heapify(A,smaller)

    def solve(self, A, B):
        heap=[]
        for i in range(len(A)):
            heap.append([A[i],A[i]])
        for i in range(len(A)//2-1,-1,-1):
            self.heapify(heap,i)
        while B>0:
            heap[0][0]+=heap[0][1]
            self.heapify(heap,0)
            B-=1
        max_val=0
        for i in range(len(heap)):
            max_val=max(max_val,heap[i][0])
        return max_val

obj=Solution()
A=[8,6,4,2]
B=8
print(obj.solve(A,B))