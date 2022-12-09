def solve(A, B):    
    data={}
    for i in range(len(A)):
        if A[i]%B in data:
            data[A[i]%B]+=1
        else:
            data[A[i]%B]=1
    count=0
    for i in range(B//2+1):
        if i==0 and i in data:
            count+= data[i]*(data[i]-1)/2
        elif B-i==i and i in data and B-i in data:
            count+=data[i]*(data[i]-1)/2
        elif i in data and B-i in data:
            count+=data[i]*data[B-i]
    
    if B%2==0 and B//2+1 in data:
        count+=data[B//2+1]*(data[B//2+1]-1)/2
    
    return int(count%1000000007)

A=[ 93, 9, 46, 79, 56, 24, 10, 26, 9, 93, 31, 93, 75, 7, 4, 80, 19, 67, 49, 84, 62, 100, 17, 40, 35, 84, 14, 81, 99, 31, 100, 66, 70, 2, 11, 84, 60, 89, 13, 57, 47, 60, 59, 60, 42, 67, 89, 29, 85, 83, 42, 47, 66, 80, 88, 85, 83, 82, 16, 23, 21, 55, 26, 2, 21, 92, 85, 26, 46, 3, 7, 95, 50, 22, 84, 52, 57, 44, 4, 23, 25, 55, 41, 49 ]
B=37
#A=[1,2,3,4,5]
#B=2
A=[ 69, 50, 9, 94, 94, 100, 11, 30, 57, 83, 71, 40, 75, 53, 12, 62, 15, 38, 30, 78, 10, 42, 74, 31, 42, 13, 20, 66, 74, 15, 67, 23, 50, 71, 3, 86, 9, 52, 56, 92, 60, 55, 30, 87, 2 ]
B=21
print(solve(A,B))