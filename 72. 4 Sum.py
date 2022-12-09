def fourSum(A, B):
    A.sort()
    map_ = {}
    for i in range(len(A)):
        if A[i] not in map_:
            map_[A[i]] = 1
        else:
            map_[A[i]] += 1

    result = []
    for i in range(len(A)-3):
        for j in range(i+1, len(A)):
            for k in range(j+1, len(A)): 
                left_num = B-A[i]-A[j]-A[k]
                if left_num in map_ and left_num>=A[k]:
                    result.append([A[i],A[j],A[k],left_num])
    return result


A = [23, 20, 0, 21, 3, 38, 35, -6, 2, 5, 4, 21]
B = 29
print(fourSum(A, B))

# [0 2 4 23 ] [0 3 5 21 ] [0 4 5 20 ] [2 3 4 20 ]
