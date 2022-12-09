def solve1(A):
    sum_=0
    
    sum_=0
    for i in range (len(A)):
        sub_or=0
        or_=0
        for j in range(i,len(A)):
            or_=or_|A[j]%(pow(10,9)+7)
            sub_or+=or_%(pow(10,9)+7)
        
        sum_+=sub_or%(pow(10,9)+7)
    
    return sum_%(pow(10,9)+7)
    
def solve2(A):    
    result=0

    for i in range(31):
        bit=len(A)
        for j in range(len(A)-1,-1,-1):
            if (A[j]>>i)&1==1:
                bit=j
            result+=(len(A)-bit)*(1<<i) %(pow(10,9)+7)
    
    return result

# Python 3 program to find sum of bitwise OR of all subarrays
# from math lib. import log2 function
from math import log2
# Function to find sum of bitwise OR of all subarrays
def solve3(A):
    n=len(A)
    # Find max element of the array
    max_element = max(A)
    # Find the max bit position set in the array
    maxBit = int(log2(max_element)) + 1
    totalSubarrays = n * (n + 1) // 2
    s = 0
    # Traverse from 1st bit to last bit which can be set in any element of the array
    for i in range(maxBit) :
        c1 = 0
        # List to store indexes of the array with i-th bit not set
        vec = []
        sum = 0
        # Traverse the array
        for j in range(n) :
            # Check if ith bit is not set in A[j]
            a = A[j] >> i
            if (not(a & 1)) :
                vec.append(j)
        # Variable to store count of subarrays whose bitwise OR will have i-th bit not set
        cntSubarrNotSet = 0
        cnt = 1
        for j in range(1, len(vec)) :
            if (vec[j] - vec[j - 1] == 1) :
                cnt += 1
            else :
                cntSubarrNotSet += cnt * (cnt + 1) // 2
                cnt = 1
        # For last element of vec
        cntSubarrNotSet += cnt * (cnt + 1) // 2
        # If vec is empty then cntSubarrNotSet should be 0 and not 1
        if len(vec) == 0:
            cntSubarrNotSet = 0
        # Variable to store count of subarrays whose bitwise OR will have i-th bit set
        cntSubarrIthSet = totalSubarrays - cntSubarrNotSet
        s += cntSubarrIthSet * pow(2, i)
    return s


A=[1,2,3,4,5]
print(solve3(A))