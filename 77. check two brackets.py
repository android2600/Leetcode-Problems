def solve(A, B):
    hashmap1={}
    stack=[]
    stack.append(1)
    operators=("+","-","(",")")
    sign=1
    for i in range(len(A)):
        if A[i] not in operators:
            if i==0:
                hashmap1[A[i]]=1
            elif i>0:
                if A[i-1]=="+" or A[i-1]=="(":
                    hashmap1[A[i]]=sign
                elif A[i-1]=="-":
                    hashmap1[A[i]]=-sign
        else:
            if A[i]=="(":
                if i==0:
                    stack.append(1)
                else:
                    if A[i-1]=="-":
                        stack.append(-1)
                        sign*=-1
                    else:
                        stack.append(1)
            elif A[i]==")":
                sign*=stack.pop()
    hashmap2={}
    stack=[]
    stack.append(1)
    for i in range(len(B)):
        if B[i] not in operators:
            if i==0:
                hashmap1[B[i]]=1
            elif i>0:
                if B[i-1]=="+" or B[i-1]=="(":
                    hashmap1[A[i]]=sign
                elif B[i-1]=="-":
                    hashmap1[B[i]]=-sign
        else:
            if B[i]=="(":
                if i==0:
                    stack.append(1)
                else:
                    if B[i-1]=="-":
                        stack.append(-1)
                    else:
                        stack.append(1)
            elif B[i]==")":
                sign*=stack.pop()
    
    for x in hashmap1:
        if x not in hashmap2:
            return 0
        else:
            if hashmap1[x]!=hashmap2[x]:
                return 0
    return 1
A ="(a+b-c-d+e-f+g+h+i)"
B ="a+b-c-d+e-f+g+h+i"
A = "-(-(-(-a+b)-d+c)-q)"
B = "a-b-d+c+q"
print(solve(A,B))