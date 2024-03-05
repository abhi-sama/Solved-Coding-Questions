# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        hl=self.maxDepth(root.left)
        if hl==-1:
            return -1
        hr=self.maxDepth(root.right)
        if hr==-1:
            return -1
        if abs(hl-hr)>1:
            return -1
        return 1+max(hl,hr)   
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.maxDepth(root)!=-1       