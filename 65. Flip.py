def flip(A):
    #kadane
    str_array=[0]*len(A)
    for i in range(len(A)):
        if A[i]=="0":
            str_array[i]=1
        else:
            str_array[i]=-1
    
    current_max=0
    total_max=0
    left_index=0
    right_index=0
    current_left_index=0
    for i in range(len(A)):
        current_max+=str_array[i]
        if total_max<current_max:
            total_max=current_max
            right_index=i
            left_index=current_left_index
        if current_max<0:
            current_max=0
            current_left_index=i+1
    return ([] if total_max==0 else [left_index+1,right_index+1])


A="011"
print(flip(A))