class Solution:
    # @param A : list of list of chars
    def __init__(self):
        self.solved=False

    def check(self,A,i,j,num):
        for k in range(len(A)):# Row
            if A[k][j]==num:
                return False
        for k in range(len(A)):# Column
            if A[i][k]==num:
                return False
        for k in range(i-i%3,i+3-i%3):# Grid
            for l in range(j-j%3,j+3-i%3):
                if A[k][l]==num:
                    return False
        return True # Safe to place

    def backtracking(self,A,i,j):
        if A[i][j]!=".":
            self.backtracking(A,i,j+1)
            
        if i==len(A)-1 and j==len(A)-1:
            self.solved=True
            return True
        
        if j==len(A):
            j=0
            i=i+1

        for k in range(1,10):
            if self.check(A,i,j,chr(k)):
                A[i][j]=chr(k)
                self.backtracking(A,i,j+1)
                if not self.solved:
                    A[i][j]="."
        return False

    def solveSudoku(self, A):
        self.backtracking(A,0,0)
        return A

obj=Solution()
A=[ "53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79" ]
print(obj.solveSudoku(A))
