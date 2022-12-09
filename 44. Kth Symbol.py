def solve( A, B):
        if(1<<(A-1)==2):
            return 0
        section=solve(A-1,B//2)
        if B%2==1:
            return 1-section
        else:
            return section

print(solve(5,13))