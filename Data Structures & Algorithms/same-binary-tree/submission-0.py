# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.baby=True
        def compare(node1,node2):
            if node1==None and node2==None:
                return
            elif node1==None and node2!=None:
                self.baby=False
                return
            elif node1!=None and node2==None:
                self.baby=False
                return 
            if node1.val!=node2.val:
                self.baby=False
            compare(node1.left,node2.left)
            compare(node1.right,node2.right)
        compare(p,q)
        return self.baby



        
