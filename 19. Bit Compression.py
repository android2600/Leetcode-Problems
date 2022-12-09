def compressBits(A):
        num=0
        for i in range(0,len(A)):
            for j in range(i+1,len(A)):
                A[i]=A[i]&A[j]
                A[j]=A[i]|A[j]
                print(A)
        #print(A)
        for i in range(0,len(A)):
            num=num^A[i]   
        print(num)

compressBits([1, 3, 5])