import logging
def solve(A):
    odd=[0]*len(A)
    even=[0]*len(A)
    even[0]=A[0]
    for i in range(0,len(A)):
        if(i%2==0):
            even[i]=even[i-1]+A[i]
            if(i>0):
                odd[i]=odd[i-1]
            else:
                odd[0]=0
        else:
            odd[i]=odd[i-1]+A[i]
            even[i]=even[i-1]
    print(odd)
    print(even)
    count=0
    for i in range(0,len(A)):
        if(i>0):
            if(even[len(A)-1]-even[i]+odd[i-1]==odd[len(A)-1]-odd[i]+even[i-1]):
                count+=1
        else:
            if(even[len(A)-1]-even[i]==odd[len(A)-1]-odd[i]):
                count+=1
    return count
print(solve([1,1,1]))