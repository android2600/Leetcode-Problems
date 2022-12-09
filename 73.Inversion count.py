class Solution:
    # @param A : list of integers
    # @return an integer
    def merge(self,left_array,right_array,A):
        l_l=len(left_array)
        l_r=len(right_array)
        i,j,k=0,0,0
        count=0
        while i<l_l and j<l_r:
            if left_array[i]<right_array[j]:
                A[k]=left_array[i]
                i+=1
            else:
                A[k]=right_array[j]
                count=count+1
                j+=1
            k+=1
        while i<l_l:
            A[k]=left_array[i]
            k+=1
            i+=1
        while j<l_r:
            A[k]=right_array[j]
            j+=1
            k+=1
        return count
    
    def mergesort(self,A):
        if len(A)==1:
            return 0
        left_array=A[:len(A)//2]
        right_array=A[len(A)//2:]
        left_num=self.mergesort(left_array)
        right_num=self.mergesort(right_array)
        return left_num+right_num+self.merge(left_array,right_array,A)
    
    def solve(self, A):
        return self.mergesort(A)
        

A=[ 28, 18, 44, 49, 41, 14 ]
#A=[ 45, 10, 15, 25, 50 ]
obj=Solution()
print(obj.solve(A))