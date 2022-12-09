k=3
A=input()
A=A.split()
A=[int(a) for a in A]
A=A[1:]
#A=[1,2,3,4,5,6,7,8,9]

for i in range(0,int(len(A)/2)):
    temp=A[i]
    A[i]=A[len(A)-i-1]
    A[len(A)-i-1]=temp
for i in range(0,int(k/2)):
    temp=A[i]
    A[i]=A[k-i-1]
    A[k-i-1]=temp
num=0
for i in range(k,int((len(A)+k)/2)):
    temp=A[i]
    A[i]=A[len(A)-num-1]
    A[len(A)-num-1]=temp
    num+=1
print(A)
