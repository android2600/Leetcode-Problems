class Node:
    def __init__(self):
        self.data={}
        self.size={}

class Solution:
    # @param A : list of integers
    # @param B : list of strings
    # @return a list of integers
    def __init__(self):
        self.dictionary=Node()
    
    def add(self,word):
        n=len(word)
        root=self.dictionary
        for i in range(n):
            if word[i] in root.data:
                root.size[word[i]]+=1
            else:
                temp=Node()
                root.data[word[i]]=temp
                root.size[word[i]]=1
            root= root.data[word[i]]

    def find(self,word):
        n=len(word)
        root=self.dictionary
        size=0
        for i in range(n):
            if word[i] not in root.data:
                return 0
            else:
                size=root.size[word[i]]
                root=root.data[word[i]]
        return size

    def solve(self, A, B):
        result=[]
        for i in range(len(A)):
            if A[i]==0:
                self.add(B[i])
            else:
                count=self.find(B[i])
                result.append(count)
        return result

A = [ 0, 0, 1, 1 ]
B = [ "hack", "hacker", "hac", "hak" ]

obj=Solution()
print(obj.solve(A,B))