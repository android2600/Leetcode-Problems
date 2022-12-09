class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList:
    def __init__(self):
        self.head=None
        self.length=0

    def add(self,value):
        new=ListNode(value)
        temp=self.head
        self.head=new
        new.next=temp
        self.length+=1

    def append(self,value):
        if self.length==0:
            self.head=ListNode(value)
            self.length+=1
            return
        #print(self.length)
        new=ListNode(value)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=new
        self.length+=1

    def insert(self,value,index):
        if index>self.length:
            return
        elif index==0:
            self.add(value)
        elif index==self.length:
            new=ListNode(value)
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=new
            self.length+=1
        else:
            new=ListNode(value)
            temp=self.head
            c=0
            while c<index-1:
                temp=temp.next
                c+=1
            t=temp.next
            temp.next=new
            new.next=t
            self.length+=1

    def delete(self,index):
        if index>self.length-1:
            return
        else:
            c=0
            prev=None
            curr=self.head
            if index==0:
                self.head=curr.next
                if self.length>0:
                    self.length-=1
                return
            
            while c<index:
                prev=curr
                curr=curr.next
                c+=1
            if self.length-1==index:
                prev.next=None
                #print("hi")
            elif self.length-1>index:    
                prev.next=curr.next
                #print("hi")
            self.length-=1


class Solution:
    # @param A : list of list of integers
    # @return the head node in the linked list
    def solve(self, A):
        llist=LinkList()
        for i in range(len(A)):
            if A[i][0]==0:
                llist.add(A[i][1])
                #print(i)
            elif A[i][0]==1:
                llist.append(A[i][1])
                #print(i)
            elif A[i][0]==2:
                llist.insert(A[i][1],A[i][2])
                #print(i)
            elif A[i][0]==3:
                llist.delete(A[i][1])
                #print(i)
            print(llist.length)
        n=llist.head
        nodes = []
        while n:
            nodes.append(str(n.val))
            n = n.next
        nodes.append("None")
        return " -> ".join(nodes)
"""      
A=[
  [1, 13, -1],
  [3, 0, -1],
  [3, 1, -1],
  [2, 15, 0],
  [3, 0, -1],
  [1, 12, -1],
  [3, 0, -1],
  [1, 19, -1],
  [1, 13, -1],
  [3, 0, -1],
  [0, 12, -1],
  [1, 13, -1],
  [3, 2, -1]
]
"""
"""
A=[
  [3, 1, -1],
  [1, 15, -1],
  [3, 0, -1],
  [0, 10, -1],
  [0, 18, -1],
  [1, 19, -1],
  [2, 6, 2],
  [0, 11, -1]
]
"""
"""
A=[
  [2, 18, 0],
  [2, 5, 1],
  [2, 8, 0],
  [1, 7, -1],
  [1, 5, -1]
]
"""
"""
A=[
  [3, 1, -1],
  [3, 1, -1],
  [1, 18, -1],
  [2, 12, 1],
  [1, 17, -1],
  [2, 11, 3],
  [1, 19, -1],
  [3, 0, -1],
  [0, 12, -1]
]
"""
A =[
  [1, 13, -1],
  [3, 0, -1],
  [3, 1, -1],
  [2, 15, 0],
  [3, 0, -1],
  [1, 12, -1],
  [3, 0, -1],
  [1, 19, -1],
  [1, 13, -1],
  [3, 0, -1],
  [0, 12, -1],
  [1, 13, -1],
  [3, 2, -1]
]
temp=Solution()
print(temp.solve(A))