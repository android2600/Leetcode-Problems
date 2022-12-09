def generateMatrix(A): # Use variables for direction
    B=[[0]*A for i in range(0,A)]
    num=1
    for k in range(0,A-2):
        row=k
        col=k
        for i in range(0,4*(A-1-2*k)):
            if(row==k and col<A-k):
                B[row][col]=num
                num+=1
                col+=1
            if(col==A-k and row<A-k-1):
                B[row+1][col-1]=num
                num+=1
                row+=1
            if(row==A-k-1 and col>k):
                B[row][col-1]=num
                num+=1
                col-=1
            if(row>k and col==k):
                B[row-1][col]=num
                num+=1
                row-=1
    print(B)

generateMatrix(4)