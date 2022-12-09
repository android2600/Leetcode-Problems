from unittest import result


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return a list of list of integers
    def solve(self, A, B): #max heap
        heap=[]
        i=0
        while len(heap)<len(A):
            heap.append(A[i])
            n=len(heap)-1
            p=(n-1)//2
            #parent=heap[p]
            #child=heap[n]
            parent=heap[p][0]*heap[p][0]+heap[p][1]*heap[p][1]
            child=heap[n][0]*heap[n][0]+heap[n][1]*heap[n][1]
            while n!=0 and parent<child:
                heap[p],heap[n]=heap[n],heap[p]
                n=p
                p=(n-1)//2
                #parent=heap[p]
                #child=heap[n]
                parent=heap[p][0]*heap[p][0]+heap[p][1]*heap[p][1]
                child=heap[n][0]*heap[n][0]+heap[n][1]*heap[n][1]
            i+=1
        result=[]
        for i in range(B):
            heap[0],heap[len(heap)-1]=heap[len(heap)-1],heap[0]
            result.append(heap.pop())
        return heap

A =[
  [-762, 643],
  [693, -1004],
  [-1026, 680],
  [722, -1092],
  [-875, 630],
  [787, -860],
  [-807, 999],
  [1015, -788],
  [-760, 889],
  [990, -642],
  [-1098, 1044],
  [863, -614],
  [-744, 651],
  [959, -898],
  [-905, 926],
  [808, -725],
  [-730, 809],
  [871, -908],
  [-993, 957],
  [658, -924],
  [-927, 872],
  [735, -821],
  [-1069, 1018],
  [839, -777],
  [-957, 786],
  [853, -942],
  [-865, 955],
  [705, -1072],
  [-717, 940],
  [922, -618],
  [-1013, 802],
  [1065, -884],
  [-638, 1063],
  [654, -882],
  [-722, 718],
  [703, -870],
  [-837, 1059],
  [723, -747],
  [-869, 620],
  [951, -625],
  [-890, 693],
  [1043, -927],
  [-745, 636],
  [976, -951],
  [-1055, 711],
  [658, -867],
  [-1011, 1049],
  [867, -624],
  [-685, 1018],
  [1018, -962],
  [-1070, 885],
  [954, -798],
  [-1005, 1095],
  [-370, 81],
  [156, -484],
  [-286, 228],
  [476, -87],
  [-450, 114],
  [86, -315],
  [-89, 466],
  [383, -447]
]
#A= [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
B = 8
obj=Solution()
print(obj.solve(A,B))