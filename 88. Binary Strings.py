def solve(A, B):
        data=[x for x in A]
        i=0
        count=0
        if len(data)==2 and (data[0]=="0" or data[1]=="0"):
            return -1
        if len(data)==1 and data[0]=="0":
            return -1
        while i<=len(data)-3:
            if (i==294 or i==295 or i==296):
                print("")
            if data[i]=="1":
                i+=1
            else:
                if i+2<len(data) and data[i+1]=="0" and data[i+2]=="0":
                    data[i],data[i+1],data[i+2]="1","1","1"
                    i+=3
                    count+=1
                elif i+2<len(data) and data[i+1]=="0" and data[i+2]=="1":
                    data[i],data[i+1],data[i+2]="1","1","0" 
                    i+=2
                    count+=1
                elif i+2<len(data) and data[i+1]=="1" and data[i+2]=="1":
                    data[i],data[i+1],data[i+2]="1","0","0"
                    i+=1
                    count+=1
                elif i+2<len(data) and data[i+1]=="1" and data[i+2]=="0":
                    data[i],data[i+1],data[i+2]="1","0","1"
                    i+=1
                    count+=1
                else:
                    i+=1
        if data[len(data)-1]=="0" or data[len(data)-2]=="0":
            return -1
        return count

A="0111111111100"
B=2
A="00010110"
B=3
A="01000101011010001100001110010010011011110100110011001011111110110011011111100011110111000110010100111100011101100110011000110111101010101110011001111111100010100101101101110011110011111111001000100010100010111100101100010101001111111111111010111111111000110011110000010011111100000011100110001001"
B=160
print(solve(A,B))