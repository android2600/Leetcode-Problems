def solve(A, B):
    graph=[[] for i in range(A+1)]
    visited_count=[0 for i in range(A+1)]
    for i in range(len(B)):
        graph[B[i][0]].append(B[i][1])
        visited_count[B[i][1]]+=1
    result=[]
    visited=[False for i in range(A+1)]
    queue=[]
    for i in range(1,A+1):
        if visited_count[i]==0:
            queue.append(i)
            visited[i]=True
            break
    while queue:
        curr=queue.pop(0)
        result.append(curr)
        visited[curr]=True
        for i in range(len(graph[curr])):
            x=graph[curr][i]
            if visited_count[x]>0:
                visited_count[x]-=1
        for i in range(1,A+1):
            if visited[i]==False and visited_count[i]==0:
                queue.append(i)
                break
    return result

A = 8
B =[
  [1, 4],
  [1, 2],
  [4, 2],
  [4, 3],
  [3, 2],
  [5, 2],
  [3, 5],
  [8, 2],
  [8, 6]
]
A = 6
B = [
  [6, 3],
  [6, 1],
  [5, 1],
  [5, 2],
  [3, 4],
  [4, 2]
]
print(solve(A,B))
