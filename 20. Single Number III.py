def solve(A):
        res1=0
        res2=0
        num=0

        for i in range(0,len(A)):
            num=num^A[i]
        #print(num)
        #print(~(num-1))
        temp=num&(~(num-1))
        #print(temp&4)
        for i in range(0,len(A)):
            if(temp&A[i]!=0):
                res1=res1^A[i]
            else:
                res2=res2^A[i]
        print(res1,res2)
            #if(res1>res2):
            #    return [res2,res1]
            #else:
            #    return [res1,res2]

print(solve([3,4,2,4,3,5]))