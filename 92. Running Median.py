import heapq
def solve(A):
    result=[]
    heap_min=[]
    heap_max=[]
    heap_max.append(-A[0])
    result.append(A[0])
    for i in range(1,len(A)):
        if A[i]>-heap_max[0]:
            heapq.heappush(heap_min,A[i])
        else:
            heapq.heappush(heap_max,-A[i])

        if len(heap_max)==len(heap_min)+2:
            temp=heapq.heappop(heap_max)
            heapq.heappush(heap_min,-temp)
        
        if len(heap_max)+1==len(heap_min):
            temp=heapq.heappop(heap_min)
            heapq.heappush(heap_max,-temp)

        result.append(-heap_max[0])
    return result

A=[ 59, 64, 10, 39 ]
A=[ 32, 91, 86, 8, 4, 100, 98, 15, 79, 32, 4, 99 ]
print(solve(A))