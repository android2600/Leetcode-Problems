class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge_sort(self,lA,rA,A):
        nl=len(lA)
        nr=len(rA)
        i,j,k=0,0,0
        while(i<nl and j<nr):
            if lA[i][0]>rA[j][0]:
                A[k]=rA[j]
                j+=1
            else:
                A[k]=lA[i]
                i+=1
            k+=1
        while i<nl:
            A[k]=lA[i]
            i+=1
            k+=1
        while (j<nr):
            A[k]=rA[j]
            j+=1
            k+=1

    def sort(self,A):
        lA=A[:int(len(A)//2)]
        rA=A[int(len(A)//2):]
        if len(A)<2:
            return
        else:
            self.sort(lA)
            self.sort(rA)
            self.merge_sort(lA,rA,A)

    def merge(self, intervals):
        self.sort(intervals)
        result=[]
        result.append([intervals[0][0],intervals[0][1]])
        i=1
        j=0
        #print(intervals)
        while(i<len(intervals)):
            if result[j][0]<=intervals[i][0] and intervals[i][1]<=result[j][1]:
                i+=1
            elif result[j][0]<=intervals[i][0] and intervals[i][0]<=result[j][1]:
                result[j][1]=intervals[i][1]
                i+=1
            else:
                result.append([intervals[i][0],intervals[i][1]])
                j+=1
                i+=1
        return result

    def insert(self, intervals, newInterval):
        index=0
        for i in range(len(intervals)):
            if (newInterval[0]>=intervals[i][0]) :
                index=i
        print(intervals[index][0],intervals[index][1])
        print(newInterval[0],newInterval[1])
        result=[]
        if newInterval[0]<=intervals[index][1] and newInterval[1]<=intervals[index][1]:
            print("1")
            result=self.merge(intervals)
        elif (newInterval[0]>intervals[index][1] and index==len(intervals)-1):
            print("2")
            result=self.merge(intervals[:index+1]+[newInterval])
        else:
            print("3")
            result=self.merge(intervals[:index+1]+[newInterval]+intervals[index+1:])
        return result
res_=Solution()
A=[ [4, 100], [48, 94], [102, 121], [58, 71], [36, 53], [49, 68], [18, 42], [37, 90], [68, 75], [6, 57], [25, 78], [58, 79], [18, 29], [69, 94], [5, 31], [10, 87], [21, 35], [1, 32], [7, 24], [17, 85], [30, 95], [5, 63], [1, 17], [67, 100], [53, 55], [30, 63], [7, 76], [33, 51], [62, 68], [78, 83], [12, 24], [31, 73], [64, 74], [33, 40], [51, 63], [17, 31], [14, 29], [9, 15], [39, 70], [13, 67], [27, 100], [10, 71], [18, 47], [48, 79], [70, 73], [44, 59], [68, 78], [24, 67], [32, 70], [29, 94], [45, 90], [10, 76], [12, 28], [31, 78], [9, 44], [29, 83], [21, 35], [46, 93], [66, 83], [21, 72], [29, 37], [6, 11], [56, 87], [10, 26], [11, 12], [15, 88], [3, 13], [56, 70], [40, 73], [25, 62], [63, 73], [47, 74], [8, 36] ]
A=[ [6037774, 6198243], [6726550, 7004541], [8842554, 10866536], [11027721, 11341296], [11972532, 14746848], [16374805, 16706396], [17557262, 20518214], [22139780, 22379559], [27212352, 28404611], [28921768, 29621583], [29823256, 32060921], [33950165, 36418956], [37225039, 37785557], [40087908, 41184444], [41922814, 45297414], [48142402, 48244133], [48622983, 50443163], [50898369, 55612831], [57030757, 58120901], [59772759, 59943999], [61141939, 64859907], [65277782, 65296274], [67497842, 68386607], [70414085, 73339545], [73896106, 75605861], [79672668, 84539434], [84821550, 86558001], [91116470, 92198054], [96147808, 98979097] ]
B=[36210193, 61984219]
A=[ [1, 2], [8, 10] ]
B=[3,6]
print(res_.insert(A,B))