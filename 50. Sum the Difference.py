def solve(A):
    A.sort()
    sum_=0
    for i in range(len(A)):
        add_count=(1<<i)-1
        sub_count=(1<<(len(A)-i-1))-1
        sum_+= A[i]*(add_count-sub_count)

    return sum_
A=[5,4,2]
print(solve(A))