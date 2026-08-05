# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.baby=True
        def dfs(node):
            if node==None:
                return 0
            lh=dfs(node.left)
            rh=dfs(node.right)
            if abs(rh-lh)>1:
                self.baby=False
            return 1+max(lh,rh)
        dfs(root)
        return self.baby