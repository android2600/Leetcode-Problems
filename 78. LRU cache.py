class DLLNode:
    def __init__(self, value):
        self.value=value
        self.next=None
        self.prev=None

class LRUCache:
    def addAtHead(self, key):
        newNode=self.DLLNode(key)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    
    def deleteTailNode(self):
        if self.tail==self.head: # only 1 node
            self.tail = None
            self.head = None
        else:
            self.tail = self.tail.prev
            if self.tail!=None:
                self.tail.next = None
    
    def updateList(self, key):
        # bring the key at the head
        if self.head==self.tail: # only 1 element nothing to do
            return
        curr = self.head
        while curr!=None:
            if curr.value==key:
                break
            curr=curr.next
        if curr==self.head:
        # nothing to do
            return
        elif curr==self.tail:
            self.deleteTailNode()
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.addAtHead(key)

# @param capacity, an integer
    def __init__(self, capacity):
        self.capacity=capacity
        self.data={}
        self.head=None
        self.tail=None
    # @return an integer
    def get(self, key):
        if key in self.data:
            self.updateList(key)
            return self.data[key]
        else:
            return -1
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.data:
            self.updateList(key)
        else:
            size = len(self.data)
        if size<self.capacity:
            self.addAtHead(key)
        else:
            if self.tail!=None:
                temp = self.tail.value
            del self.data[temp]
            self.deleteTailNode()
            self.addAtHead(key)
            self.data[key]=value