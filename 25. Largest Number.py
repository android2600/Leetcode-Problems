def largestNumber(A):
        B=""
        k=0
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                k=0
                if(int(str(A[i])[k])<=int(str(A[j])[k])):
                    temp=A[i]
                    A[i]=A[j]
                    A[j]=temp
                if(int(str(A[i])[k])==int(str(A[j])[k])):
                    if(len(str(A[i]))>k+1 and len(str(A[j]))==1):
                        if(int(str(A[i])[k+1])==0):
                            temp=A[i]
                            A[i]=A[j]
                            A[j]=temp
                    if(len(str(A[i]))>k+1 and len(str(A[j]))>k+1):
                        k+=1
                        if(int(str(A[i])[k])<int(str(A[j])[k])):
                            temp=A[i]
                            A[i]=A[j]
                            A[j]=temp
                print(A)
        for i in range(len(A)):
            B=B+str(A[i])
        return B

A=[ 389, 305, 3,340, 5, 9 ]
print(largestNumber(A))