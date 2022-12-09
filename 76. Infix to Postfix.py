def solve(A):
    stack=[]
    operator={"^":1,"/":2,"*":2,"+":3,"-":3,"(":4}
    stack_op=[]
    result=""
    for i in range(len(A)):
        if A[i] not in operator and A[i]!=")":
            if A[i]!="(":
                stack.append(A[i])
            else:
                stack_op.append(A[i])
        
        elif A[i] not in operator and A[i]==")":
            while len(stack_op)>0 and stack_op[-1]!="(":
                stack.append(stack_op.pop())
            if len(stack_op)>0:
                stack_op.pop()

        elif A[i] in operator:
            if A[i]!="(":
                while len(stack_op)>0 and operator[stack_op[-1]]<=operator[A[i]]:
                    stack.append(stack_op.pop())
            stack_op.append(A[i])
            
    while stack_op:
        stack.append(stack_op.pop())
        

    while stack:
        result=stack.pop()+result
    
    return result
A="a*(r+o*h)"
A="q+(c*t)*o+(g*g)+q*(i-a)*p-(i*l)"
print(solve(A))