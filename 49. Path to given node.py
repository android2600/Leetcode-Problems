class TreeNode:
    def __init__(self,value) -> None:
        self.val=value
        self.left=None
        self.right=None

class path:
    def __init__(self) -> None:
        self.result=[]
    
    def search(self,A,B):
        if A==None:
            return False
        if A.val==B:
            return True
        return self.search(A.left,B) or self.search(A.right,B)
    
    def path_to_node(self, A, B):        
        root=A
        value=B
        def helper(root,value):
            if root==None:
                return False
            
            if root.val==value:
                self.result.append(root.val)
                return True

            if helper(root.left,value) or helper(root.right,value):
                self.result.append(root.val)
            
            return self.search(root.left,value) or self.search(root.right,value)
        
        helper(root,value)
        return self.result[::-1]
        



head=TreeNode(5)
head.left=TreeNode(7)
head.left.left=TreeNode(2)
head.left.right=TreeNode(3)
head.right=TreeNode(8)
head.right.left=TreeNode(6)

run_=path()
print(run_.search(head,6))
print(run_.path_to_node(head,6))