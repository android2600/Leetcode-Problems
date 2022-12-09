def addBinary(A, B):
        
        if(len(A)>len(B)):
            large=len(A)
            small=len(B)
        else:
            large=len(B)
            small=len(A)
        C=""
        carry=0
        last_sum=0
        #print(large)
        #print(small)
        for i in range(0,large):
            if(i>small):
                if(len(A)>len(B)):
                    C=str((int(A[len(A)-1-i])+carry)%2)+C
                    last_sum=(int(A[len(A)-1-i])+carry)
                else:
                    C=str((int(B[len(B)-1-i])+carry)%2)+C
                    last_sum=(int(B[len(B)-1-i])+carry)
                carry=int(last_sum/2)
                #print("<small")
                print(C)
            else:
                C=str((int(A[len(A)-1-i])+int(B[len(B)-1-i])+carry)%2)+C
                last_sum=(int(A[len(A)-1-i])+int(B[len(B)-1-i])+carry)
                carry=int(last_sum/2)
                #print(">=small")
        
        return C

print(addBinary("1010110111001101101000","1000011011000000111100110"))