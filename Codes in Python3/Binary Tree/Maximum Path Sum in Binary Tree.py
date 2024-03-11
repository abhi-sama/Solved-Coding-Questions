# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root,maxi:List[int]):
        if root==None:
            return 0
        leftsum=max(0,self.helper(root.left,maxi))
        rightsum=max(0,self.helper(root.right,maxi))
        maxi[0]=max(maxi[0],root.val+leftsum+rightsum)
        return root.val+max(leftsum,rightsum)

    def maxPathSum(self, root: Optional[TreeNode],) -> int:
        maxi=[float('-inf')]
        self.helper(root,maxi)
        return maxi[0]