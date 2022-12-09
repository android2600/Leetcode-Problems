def binary_to_decimal(num):
    bin_num=0
    i=0
    while(num>0):
        bin_num+=(num%10)*1<<i
        i+=1
        num=num//10
    return bin_num
# bit manipulation
def grey_code(A):
    res=[]
    for i in range(1<<A):
        res.append(i^i>>1)
    return res

def recursion(A):
    if A==1:
        return ["0","1"]
    ans=[]
    result=recursion(A-1)
    for i in range(len(result)):
        ans.append("0"+result[i])
    for i in range(len(result)-1,-1,-1):
        ans.append("1"+result[i])
    return ans

def grayCode(A):
    result=recursion(A)
    return [int(x) for x in result]
#print(binary_to_decimal(11001))
print(grayCode(10))
