def colorful(A):
    B=str(A)
    data={}
    for i in range(len(B)):
        product=int(B[i])
        data[product]=i
        for j in range(i+1,len(B)):
            product*=int(B[j])
            data[product]=j
    print(data,len(data),(2<<(len(B)-1))-1)
    if(len(data)==(2<<(len(B)-1))-1):
        return 1
    else:
        return 0

A=234
print(colorful(A))
