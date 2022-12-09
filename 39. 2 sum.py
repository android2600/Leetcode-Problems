
def twoSum(nums, target):
    data={}
    for i,v in enumerate(nums):
        if v in data:
            data[v].append(i)
        else:
            data[v]=[i]
    
    result_arr=[]
    
    for v in data:
        if target-v in data and v!=target-v:
            result_arr.append([data[v][0],data[target-v][0]])
        elif target-v==v and len(data[v])>1:
            result_arr.append([data[v][0],data[v][1]])

    print(result_arr)
    
    index_1=len(nums)
    index_2=len(nums)+1
    for item in result_arr:
        if item[1]<index_2 and item[1]>item[0]:
            index_1=item[0]
            index_2=item[1]
        elif item[1]==index_2 and item[1]>item[0] and item[0]<index_1:
            index_1=item[0]
    if(index_1!=len(nums)):
        return [index_1+1,index_2+1]
    else:
        return []

#A=[ 4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
#A=[ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ]
#B=-1
A=[ 0, 8, -3, -1, 7, 9, -1, 8, -2, 2, -8, -6, -7, -4, -6, -1, -6, 6, 8, -10, -6, 4, -8, 7, 6, -4, -4, -10, -6, 5, -8, -1, 10, 6, 6, -3, -3, -7, -8, -7, 4, -7, 1, -10, 5 ]

#A=[1,1]
B=2

print(twoSum(A,B))