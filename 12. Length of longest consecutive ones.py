def solve(A):
    longest_1=0
    left=0
    right=0
    count=0
    for i in range(0,len(A)):
        if(A[i]=="1"):
            count+=1

    for i in range (0,len(A)):
        if(A[i]=="0"):
            if(count>left+right):
                print(left+right+1)
                longest_1=max(longest_1,left+right+1)
            if(count<=left+right):
                longest_1=max(longest_1,left+right)
            left=right
            right=0
        else:
            right+=1
        #print(right)

    if(count>left+right):
        longest_1=max(longest_1,left+right+1)
    if(count<=left+right):
        longest_1=max(longest_1,left+right)
    
    print(longest_1)

solve("010100110101")