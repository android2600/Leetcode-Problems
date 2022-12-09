def solve(A,B):
    avg=0
    for i in range(0,B):
        avg=avg+A[i]
    least_avg=avg
    #print(avg)
    index=0
    for i in range(1,len(A)-B+1):
        avg=(avg-A[i-1]+A[i+B-1])
        #print(avg)
        if(avg<least_avg):
            least_avg=avg
            index=i
            #print("====")
            #print(least_avg,i)
            #print("====")
    print(index)

solve([ 20, 3, 13, 5, 10, 14, 8, 5, 11, 9, 1, 11 ],9)