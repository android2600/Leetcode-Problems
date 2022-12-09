def solve( A, B):
    flag=0
    min_cost=pow(10,15)
    for i in range(1,len(A)-1):
        left_min=pow(10,10)
        right_min=pow(10,10)
        for j in range(0,i):
            if(B[j]<left_min and A[j]<A[i]):
                left_min=B[j]
                flag+=1
                #print(left_min)
        for j in range(i+1,len(A)):
            if(B[j]<right_min and A[i]<A[j]):
                right_min=B[j]
                flag+=1
                #print(right_min)
        if(B[i]+left_min+right_min<min_cost):
            min_cost=B[i]+left_min+right_min
    if(flag<2):
        min_cost=-1
    print(min_cost)

#solve([ 5, 9, 10, 4, 7, 8 ],[ 5, 6, 4, 7, 2, 5 ])
solve([ 100, 101, 100 ],[2,4,5])
solve([ 802030518, 598196518, 640274071, 983359971, 71550121, 96204862, 799843967, 446173607, 796619138, 402690754 ],[ 23219513, 68171337, 12183499, 5549873, 73542337, 66661387, 79397647, 34495917, 31413076, 50918417 ])
