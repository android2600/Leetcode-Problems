class Solution:
    # @param A : list of list of integers
    # @return an integer
    def update(self,queue,A,i,j):
        k=[0,0,1,-1]
        l=[-1,1,0,0]
        for m in range(len(k)):
            if (i==len(A)-1 and k[m]==1) or (j==len(A[0])-1 and l[m]==1) or (i==0 and k[m]==-1) or (j==0 and l[m]==-1):
                continue
            elif A[i+k[m]][j+l[m]]==1:
                A[i+k[m]][j+l[m]]=2
                queue.append((i+k[m],j+l[m]))

    def solve(self, A):# BFS
        queue=[]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==2:
                    queue.append((i,j))
        queue.append("")
        count=0
        while len(queue)>1:
            curr=queue.pop(0)
            if curr=="":
                count+=1
                queue.append("")
            else:
                if A[curr[0]][curr[1]]==2:
                    A[curr[0]][curr[1]]=0
                    self.update(queue,A,curr[0],curr[1])
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]==1:
                    return -1
        return count

obj=Solution()
A=[
  [1, 1, 1, 2, 1, 2],
  [1, 2, 0, 0, 0, 1],
  [1, 2, 0, 1, 1, 2],
  [1, 0, 1, 2, 2, 2],
  [1, 1, 2, 1, 1, 2],
  [2, 2, 2, 2, 2, 0],
  [1, 1, 0, 1, 2, 1],
  [0, 2, 0, 0, 1, 0],
  [0, 0, 2, 1, 2, 2]
]
print(obj.solve(A))