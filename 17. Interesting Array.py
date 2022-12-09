def solve(A):
    merge=0
    for i in range(0,len(A)):
        merge=merge^A[i]
    result=""
    if(merge%2==0):
        result="Yes"
    else:
        result="No"
    return result


print(solve([9,17]))