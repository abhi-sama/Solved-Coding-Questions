# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return 0
            lh=helper(node.left)
            if lh==-1:
                return -1
            rh=helper(node.right)
            if rh==-1:
                return -1            
            if abs(lh-rh)>1:
                return -1
            return 1+max(lh,rh)
        
        return helper(root)!=-1

# TC=O(n)
# SC=O(n)