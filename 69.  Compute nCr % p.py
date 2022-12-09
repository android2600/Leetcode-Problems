def binary_exp(A,B,C):
    result =1
    while B>0: 
        if B&1:
            result=(result*A)%C
        A=(A*A)%C
        B=B>>1
    return result

def solve(A, B, C):
    result=A*binary_exp(B,C-2,C)
    for i in range(1,B):
        result=(result*(A-i)*binary_exp(i,C-2,C))%C

    return result

A=95120
B=90731
C=4184797
print(solve(A,B,C))