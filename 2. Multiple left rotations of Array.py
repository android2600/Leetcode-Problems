class Solution:
    def solve(self, A, B):
        result=[]
        for i in range (0,len(B)):
            k=B[i]%len(A)
            C=[a for a in A]

            for i in range(0,int(len(A)/2)):
                C[i]=A[len(A)-i-1]
                C[len(A)-i-1]=A[i]
            
            for i in range(0,int((len(A)-k)/2)):
                temp=C[i]
                C[i]=C[len(A)-k-i-1]
                C[len(A)-k-i-1]=temp
            num=0
            for i in range(len(A)-1,len(A)-int((k)/2+1),-1):
                temp=C[i]
                C[i]=C[len(A)-k+num]
                C[len(A)-k+num]=temp
                num+=1
            result.append(C)
        return result

res=Solution()
print(res.solve([1,2,3,4,5,6,7,8,9,10,11,12],[6,7]))
