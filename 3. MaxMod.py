
def solve(A):
        max_num=A[0]
        second_max_num=A[0]
        
        for i in range (len(A)):
            if max_num<A[i]:
                second_max_num=max_num
                max_num=A[i]
            elif second_max_num<A[i] and A[i]<max_num:
                second_max_num=A[i]
        
        return second_max_num%max_num
solve([ 927, 707, 374, 394, 279, 799, 878, 937, 431, 112 ])