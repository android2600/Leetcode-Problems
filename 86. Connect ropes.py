class Solution:
    # @param A : list of integers
    # @return an integer
    def heapifydown(self,A,index):
        if 2*index+1<len(A):
            child1=2*index+1
            child2=2*index+2
            smaller=index
            if A[child1]<A[index]:
                smaller=child1
            if child2<len(A) and A[smaller]>A[child2]:
                smaller=child2
            if smaller==index:
                return
            A[index],A[smaller]=A[smaller],A[index]
            self.heapifydown(A,smaller)
        return A
    
    def heapifyup(self,A,index):
        if index>0:
            parent=(index-1)//2
            if parent>=0 and A[parent]>A[index]:
                A[parent],A[index]=A[index],A[parent]
                self.heapifyup(A,parent)
        return A
    
    def solve(self, A):
        cost=0
        heap=[]
        for i in range(len(A)):
            heap.append(A[i])
            self.heapifyup(heap,len(heap)-1)
        
        while len(heap)>1:
            heap[0],heap[len(heap)-1]=heap[len(heap)-1],heap[0]
            temp=heap.pop()
            self.heapifydown(heap,0)
            cost+=heap[0]+temp
            heap[0]+=temp
            self.heapifydown(heap,0)
        return cost


obj=Solution()
A=[ 16, 7, 3, 5, 9, 8, 6, 15 ]
A=[ 6, 19, 9, 14, 17, 16, 7, 2, 14, 4, 3 ]
print(obj.solve(A))