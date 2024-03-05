# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[]
        ans=[]
        if root==None:
            return ans
        q.append(root)
        while q:
            qsize=len(q)
            level=[]
            for i in range(qsize):
                node=q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                level.append(node.val)
            ans.append(level)
        return ans