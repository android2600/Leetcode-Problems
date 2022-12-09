import math

def solve(A):
    max_num=max(A)
    print(max_num)
    bit_size=int(math.log(max_num,2))
    max_satisfaction=0
    print(bit_size)
    for i in range(bit_size,-1,-1):
        #print(A)
        count_one=0
        for j in range(len(A)):
            if (A[j]>>i)&1==1:
                #print(A[j])
                count_one+=1
        if count_one>=4:
            for j in range(len(A)):
                if (A[j]>>i)&1==0:
                    A[j]=0
            max_satisfaction+= (1<<i)
    return max_satisfaction

A=[ 61, 67, 7, 99, 7, 127, 7, 255, 58, 38, 68 ]
print(solve(A))