def fact(A):
    if A==0:
        return 0
    result=1
    while A>1:
        result*=A%1000003
        A-=1
    return result%1000003
def binary_exp(A,B,C):
    result=1
    while B>0:
        if B&1==1:
            result=result*A%C
        A=A*A%C
        B=B>>1
    return result%C
        
def findRank(A):
    rank=0
    map_={}
    for i in range (len(A)):
        if A[i] in map_:
            map_[A[i]]+=1
        else:
            map_[A[i]]=1

    for i in range(len(A)):
        count_less=0
        for j in range(i+1,len(A)):
            if A[j]<A[i]:
                count_less+=1
        
        map_[A[i]]-=1
        if map_[A[i]]==0:
            map_.pop(A[i])
        
        denominator=1
        for x in map_:
            if map_[x]>1:
                denominator=denominator*fact(map_[x])%1000003
        inverse_fact=binary_exp(denominator,1000001,1000003)
        
        rank=rank+((fact(len(A)-1-i))%1000003*(inverse_fact*count_less)%1000003)%1000003
    
    return (rank+1)%1000003

A="bbbbaaaa"
print(findRank(A))