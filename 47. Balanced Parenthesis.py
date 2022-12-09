def solve(A):
        
    stack1=[]
    top1=-1
    
    for i in range(len(A)):
        if A[i]=="(" or A[i]=="{" or A[i]=="[":
            stack1.append(A[i])
            print(stack1)
            top1+=1
        elif (A[i]==")" or A[i]=="}" or A[i]=="]") and top1>=0:
            print(stack1,A[top1])
            if A[i]==")" and stack1[top1]=="(":
                stack1.pop()
                top1-=1
            elif A[i]=="}" and A[top1]=="{":
                stack1.pop()
                top1-=1
            elif A[i]=="]" and A[top1]=="[":
                stack1.pop()
                top1-=1
            else:
                return 0
            print(stack1,top1)
        
        elif (A[i]==")" or A[i]=="}" or A[i]=="]") and top1==-1:
            return 0
    
    if top1>=0:
        return 0
    else:
        return 1

A="()[]"
print(solve(A))