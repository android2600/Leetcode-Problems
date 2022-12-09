def solve(A):
    row_index=0
    left_most=-1
    
    for i in range (len(A)):
        if A[0][i]==1:
                left_most=i
                break
    
    if left_most==0:
        return 0
    #print(left_most)
    for i in range (1,len(A)):
        if A[i][left_most-1]==1:
            #print(i)
            j=left_most
            while(A[i][j]!=0 and j>=0):
                j-=1
            if j==-1:
                return i
            if j<left_most:
                row_index=i
                left_most=j+1
    
    return row_index

A=[
  [0, 0, 0, 0, 0, 1, 1, 1, 1],
  [0, 0, 0, 0, 0, 1, 1, 1, 1],
  [0, 0, 0, 0, 0, 1, 1, 1, 1],
  [0, 0, 0, 0, 0, 0, 1, 1, 1],
  [0, 0, 0, 0, 0, 0, 1, 1, 1],
  [0, 0, 0, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 0, 1, 1, 1, 1, 1],
  [0, 0, 0, 1, 1, 1, 1, 1, 1],
  [0, 0, 0, 1, 1, 1, 1, 1, 1]
]

print(solve(A))