import heapq
def solve(A, B, C):
    minheap=[]
    D=[float("inf") for i in range(A)]
    D[C]=0
    graph=[[] for i in range(A)]
    for i in range(len(B)):
        graph[B[i][0]].append([B[i][2],B[i][1]])
        graph[B[i][1]].append([B[i][2],B[i][0]])
    heapq.heappush(minheap,[0,C])
    print(graph)
    while minheap:
        distance,node=minheap[0]
        heapq.heappop(minheap)
        if D[node]!=-1 and distance>D[node]:
            continue
        for i in range(len(graph[node])):
            d,n=graph[node][i]
            if D[n]!=-1 and d>D[n]:
                continue
            D[n]=min(distance+d,D[n])
            heapq.heappush(minheap,[D[node]+d,graph[node][i][1]])
    return D

A = 6
B =[
  [0, 4, 9],
  [3, 4, 6],
  [1, 2, 1],
  [2, 5, 1],
  [2, 4, 5],
  [0, 3, 7],
  [0, 1, 1],
  [4, 5, 7],
  [0, 5, 1]
]
C = 4
print(solve(A,B,C))