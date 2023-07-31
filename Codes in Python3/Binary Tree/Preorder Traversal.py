# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr=root
        res=[]
        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr=curr.right
            else:
                prev=curr.left
                while prev.right and prev.right!=curr:
                    prev=prev.right
                if prev.right is None:
                    prev.right=curr
                    res.append(curr.val)
                    curr=curr.left
                else:
                    prev.right=None
                    curr=curr.right
        return res
        # s=[]
        # res=[]
        # while root or s:
        #     while root:
        #         res.append(root.val)
        #         s.append(root)
        #         root=root.left
        #     root=s.pop()
        #     root=root.right
        # return res