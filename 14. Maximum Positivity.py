def solve( A):
        start=0
        global_start=0
        global_end=0
        length=0
        max_length=0
        end=0
        flag=1
        for i in range(0,len(A)):
            if(A[i]<0):
                if(flag!=0):
                    end=i
                length=end-start
                if(length>max_length):
                    global_start=start
                    global_end=end
                    max_length=length
                flag=0
            if(flag==0 and A[i]>=0):    
                start=i
                flag=1
        if(flag==1 and len(A)-start>max_length):
            global_start=start
            global_end=len(A)
        print(A[global_start:global_end])

#solve([ 8986143, -5026827, 5591744, 4058312, 2210051, 5680315, -5251946, -607433, 1633303, 2186575 ])
solve([ -5173778, -8176176, 1694510, 7089884, -1394259, 1146372, -2502339, 1544618, 6602022, 4330572 ])