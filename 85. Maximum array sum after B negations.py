class Solution:
    def minheapifyup(self,heap):
        current=len(heap)-1
        parent=(current-1)//2
        while parent>=0 and heap[parent]>heap[current]:
            heap[parent],heap[current]=heap[current],heap[parent]
            current=parent
            parent=(current-1)//2
        return heap

    def minheapifydown(self,heap):
        current=0
        while 2*current+1 < len(heap):
            index=2*current+1
            if 2*current+2<len(heap) and heap[2*current+1]>heap[2*current+2]:
                    index=2*current+2
            child1=2*current+1 if 2*current+1<len(heap) else current
            child2=2*current+2 if 2*current+2<len(heap) else current
            
            if index>len(heap) or (heap[current]<=heap[child1] and heap[current]<=heap[child2]):
                break
            else:
                heap[index],heap[current]=heap[current],heap[index]
            current=index
        return heap

    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        minheap=[]
        for i in range(len(A)):
            minheap.append(A[i])
            minheap=self.minheapifyup(minheap)
        for i in range(B):
            minheap[0]*=-1
            minheap=self.minheapifydown(minheap) 
            print("")   
        return sum(minheap)

obj=Solution()
A= [ 57, 3, -14, -87, 42, 38, 31, -7, -28, -61 ]
B= 10
print(obj.solve(A,B))