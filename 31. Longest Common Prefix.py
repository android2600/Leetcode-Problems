def longestCommonPrefix(A):
    if(len(A)>1):
        index=0
        flag=0
        len_shortest_string=1000000
        index_shortest_string=0
        for i in range(len(A)):
            length=len(A[i])
            if(length<len_shortest_string):
                index_shortest_string=i
                len_shortest_string=length
        print(len_shortest_string,index_shortest_string)
        result=0
        for i in range(len_shortest_string):
            index=0
            while(index<len(A)):
                #print(i)
                if(A[index][i]==A[0][i]):
                    index+=1
                elif(A[index][i]!=A[0][i]):
                    flag=1
                    result=i
                    break
            if(flag==1):
                break
            
        if(i==len_shortest_string-1):
            result=len_shortest_string-1
        B=""
        for i in range(result):
            B=B+A[0][i]
    
    else:
        return A[0]
    
    return B
A=[ "aaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" ]

print(longestCommonPrefix(A))