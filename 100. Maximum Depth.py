class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @param F : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E, F): # BFS+Binary Search or DFS+Binary Search
        graph=[[] for i in range(A+1)]
        
        for i in range(len(B)):
            graph[B[i]].append(C[i])
            graph[C[i]].append(B[i])
        
        traverse=[False for i in range(A)]
        
        queue=[]
        queue.append([1,0]) #[node_number,level]
        level={}
        level[0]=[D[0]]
        max_depth=1
        while queue:
            curr=queue.pop(0)
            if not traverse[curr[0]-1]:
                traverse[curr[0]-1]=True
                for i in range(len(graph[curr[0]])):
                    if not traverse[graph[curr[0]][i]-1]:
                        queue.append([graph[curr[0]][i],curr[1]+1])
                        if curr[1]+1 in level:
                            level[curr[1]+1].append(D[graph[curr[0]][i]-1])
                        else:
                            level[curr[1]+1]=[D[graph[curr[0]][i]-1]]
                        max_depth=max(max_depth,(curr[1]+1)+1)
                    
        result=[]
        for i in range(len(E)):
            ans=-1
            temp=sorted(level[E[i]%max_depth])
            low=0
            high=len(temp)-1
            if F[i]>temp[high]:
                ans=-1
            elif F[i]<=temp[low]:
                ans=temp[low]
            else:
                while high>=low:
                    mid=(high+low)//2
                    if temp[mid]>F[i]:
                        ans=temp[mid]
                        high=mid-1
                    elif temp[mid]<F[i]:
                        low=mid+1
                    else:
                        ans=temp[mid]
                        break
            result.append(ans)
        return result

A = 5
B = [ 1, 4, 3, 1 ]
C = [ 5, 2, 4, 4 ]
D = [ 7, 38, 27, 37, 1 ]
E = [ 1, 1, 2 ]
F = [ 32, 18, 26 ]

A = 3
B = [ 1, 2 ]
C = [ 3, 1 ]
D = [ 7, 15, 27 ]
E = [ 1, 10, 1 ]
F = [ 29, 6, 26 ]

obj=Solution()
print(obj.solve(A,B,C,D,E,F))