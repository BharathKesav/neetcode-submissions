# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result=True
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(tree1,tree2):
            if tree1==None and tree2==None:
                return True
            if tree1==None or tree2==None or tree1.val!=tree2.val:
                return False
            else:
                return compare(tree1.left,tree2.left) and compare(tree1.right,tree2.right)
        if root==None:
            return False
        if subRoot==None:
            return True
        if compare(root,subRoot)==True:
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        