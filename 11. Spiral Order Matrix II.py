
def solve(A):
    B=[[0]*len(A[0]) for i in range(0,len(A))]
    direction=1
    num=A[0]
    for k in range(0,A-2):
        top=k
        left=k
        right=A-k
        bottom=A-k
        if(direction==1):
            for i in range(left,right):
                B[top][left]=num
            direction=2
        
        if(direction==2):
            for i in range(top+1,bottom):
                B[i][right-1]=num
            direction=3
        
        if(direction==3):
            for i in range(right-2,left-1,-1):
                B[bottom-1][i]=num
            direction=4

        if(direction==4):
            for i in range(bottom-2,top,-1):
                B[i][top]=num
            direction=1

    #edge case len(A)=1,2,3
    return B

def generateMatrix(A):
    direction=0
    top=0
    left=0
    right=A-1
    bottom=A-1
    col_index=0
    row_index=0
    result=[[0 for i in range(A)] for j in range(A)]
    for i in range(A*A):
        #print(row_index,col_index)
        if direction==0 and col_index<=right:
            result[row_index][col_index]=1+i
            if col_index==right:
                top+=1
                row_index=top
                direction=1
            if col_index!=right:
                col_index+=1
        
        elif direction==1 and row_index<=bottom:
            result[row_index][col_index]=1+i
            if row_index==bottom:
                right-=1
                col_index=right
                direction=2
            if row_index!=bottom:
                row_index+=1
        
        elif direction==2 and col_index>=left:
            result[row_index][col_index]=1+i
            if col_index==left:
                bottom-=1
                row_index=bottom
                direction=3
            if col_index!=left:
                col_index-=1
        
        elif direction==3 and row_index>=top:
            result[row_index][col_index]=1+i
            if row_index==top:
                left+=1
                col_index=left
                direction=0
            if row_index!=top:
                row_index-=1
        #print(result)
    return result  

print(generateMatrix(5))