# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode],diameter) -> int:
        if root==None:
            return 0
        hl=self.maxDepth(root.left,diameter)
        hr=self.maxDepth(root.right,diameter)
        diameter[0]=max(diameter[0],hl+hr)
        return 1+max(hl,hr) 
       
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter=[0]
        self.maxDepth(root,diameter)
        return diameter[0]