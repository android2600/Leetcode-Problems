def solve(A,B):
    prefix_sum=[0]*len(A)
    prefix_sum[0]=A[0]
    for i in range(1,len(A)):
        prefix_sum[i]=prefix_sum[i-1]+A[i]
    #print(prefix_sum)
    data={}
    for i in range(len(prefix_sum)):
        if prefix_sum[i] in data:
            pass
        else:
            data[prefix_sum[i]]=i
    #print(data)
    start_index=-1
    end_index=-1
    for v in data:
        remainder=abs(B-v)
        if remainder in data:
            print(v,remainder)
            start_index=min(data[v],data[remainder])
            end_index=max(data[v],data[remainder])
            break
    
    if(end_index==-1):
        return [-1]
    elif(start_index==-1 and end_index>-1):
        return A[:end_index+1]
    else:
        return A[start_index+1:end_index+1]

A=[ 15, 2, 48, 19, 28, 22, 44, 2, 32, 46, 46, 24, 1, 23, 49, 26, 23, 17, 17, 46, 4, 30, 40, 36, 20, 5 ]

B=82

print(solve(A,B))