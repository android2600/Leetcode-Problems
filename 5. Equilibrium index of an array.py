def solve(A):
        prefix=[0]*len(A)
        prefix[0]=A[0]
        for i in range(0,len(A)):
            prefix[i]=prefix[i-1]+A[i]
        index=-1
        #print(len(A))
        #print(prefix)
        C=[[1,3],[4,6],[7,8]]
        print(len(C))
        print(C[2][1])
        for j in range (0,len(A)):
            if(prefix[j-1]==prefix[len(A)-1]-prefix[j]):
                index=j
                break
            if(j==0 and prefix[len(A)-1]-prefix[j]==0):
                index=0
                break
            if(j==len(A)-1 and prefix[len(A)-1]-prefix[j]==0):
                index=len(A)-1
                break
        return index

print(solve([ -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25, -26, -27, -28, -29, -30, -31, -32, -33, -34, 69, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34 ]))