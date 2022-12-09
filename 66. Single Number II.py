import math
import logging
def singleNumber(A):
    logging.basicConfig(filename="log.txt",filemode="w")
    if len(A)==1:
        return A[0]
    max_num=max(A)
    print(max_num)
    num=0
    print(int(math.log(max_num,2)))
    for i in range(int(math.log(max_num,2))+1):
        index_sum=0
        for j in range(len(A)):
            index_sum+=((A[j]>>i)&1)
        logging.debug(index_sum)
        if (index_sum % 3!=0):
            print(i)
            num+=(1<<i)
    
    return num

A=[ 629, 629, 133, 133, 133, 528, 629 ]
print(singleNumber(A))