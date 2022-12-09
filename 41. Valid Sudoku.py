def isValidSudoku(A):
    for i in range(len(A)):
        data_r={}
        data_c={}
        for j in range(len(A)):
            if A[i][j]!=".":
                if A[i][j] in data_r:
                    return 0
                else:
                    data_r[A[i][j]]=1
                #print(data_r)
            if A[j][i]!=".":   
                if A[j][i] in data_c:
                    return 0
                else:
                    data_c[A[j][i]]=1
                #print(data_c)
    
    
    Arr=[[0,1,2],[3,4,5],[6,7,8]]
    k=0
    l=0
    while(k<3):
        while(l<3):
            data_r={}
            data_c={}
            for i in range(3):
                for j in range(3):
                    print(Arr[k][i],Arr[l][j])        
                    if A[Arr[k][i]][Arr[l][j]] in data_r and A[Arr[k][i]][Arr[l][j]]!=".":
                        return 0
                    else:
                        data_r[A[Arr[k][i]][Arr[l][j]]]=1
                    if A[Arr[l][j]][Arr[k][i]] in data_c and A[Arr[l][j]][Arr[k][i]]!=".":
                        return 0
                    else:
                        data_c[A[Arr[l][j]][Arr[k][i]]]=1
            l+=1
        k+=1
    return 1

A=[ "..5.....6", "....14...", ".........", ".....92..", "5....2...", ".......3.", "...54....", "3.....42.", "...27.6.." ]
A=[ "..5.....6", "....14...", ".........", ".....92..", "5....2...", ".......3.", "...54....", "3.....42.", "...27.6.." ]
print(isValidSudoku(A))