class Node:
    def __init__(self):
        self.data={}
        self.end=False

class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a strings
    def __init__(self):
        self.dictionary=Node()

    def insert(self,word):
        n=len(word)
        root=self.dictionary
        for i in range(n):
            if word[i] not in root.data:
                root.data[word[i]]=Node()
            root=root.data[word[i]]
        root.end=True

    def find(self,word):
        n=len(word)
        root=self.dictionary
        for i in range(n):
            if word[i] not in root.data:
                return False
            root=root.data[word[i]]
        return True
        
    def solve(self, A, B):
        for i in range(len(A)):
            self.insert(A[i])
        
        ans=""
        for x in B:
            flag=0
            for j in range(len(x)):
                word=list(x)
                temp=x[j]
                for k in range(0,26):
                    c=chr(ord("a")+k)
                    if c!=temp:
                        word[j]=c
                        if self.find(word):
                            ans+="1"
                            flag=1
                            break
                if flag==1:
                    break
            if flag==0:
                ans+="0"
        return ans     

A=["fly","flight","duck","duke"]
B=["sly","light","fuc","luck","duee"]
obj=Solution()
print(obj.solve(A,B))