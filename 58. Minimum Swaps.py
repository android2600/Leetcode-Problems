def solve(A, B):

    count_more=0
    count_less=0
    swap=0
    for i in range(len(A)):
        if A[i]<=B:
            count_less+=1
        if A[i]>B:
            count_more+=1
    print(count_less,count_more, A[count_less] )
    for i in range(count_less,len(A)):
        if A[i]<B:
            swap+=1
    
    return swap
    
# Working
def solve1(A, B):
    count_less=0
    max_num=0
    count=0
    for i in range(len(A)):
        if A[i]<=B:
            count_less+=1
    
    for i in range(count_less):
        if A[i]<=B:
            count+=1
    
    max_num=count
    print(count,count_less)
    for i in range(len(A)-count_less):
        if A[i]<=B:
            count-=1
        if A[i+count_less]<=B:
            count+=1
        if count>max_num:
            max_num=count        
    return count_less-max_num

A=[ 52, 7, 93, 47, 68, 26, 51, 44, 5, 41, 88, 19, 78, 38, 17, 13, 24, 74, 92, 5, 84, 27, 48, 49, 37, 59, 3, 56, 79, 26, 55, 60, 16, 83, 63, 40, 55, 9, 96, 29, 7, 22, 27, 74, 78, 38, 11, 65, 29, 52, 36, 21, 94, 46, 52, 47, 87, 33, 87, 70 ]
B=19
print(solve1(A,B))
