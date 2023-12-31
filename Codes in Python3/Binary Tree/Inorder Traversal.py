# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                    curr=curr.left
                else:
                    prev.right=None
                    res.append(curr.val)
                    curr=curr.right
        return res
        # stack=[]
        # res=[]
        # while root or stack:
        #     while root:
        #         stack.append(root)
        #         root=root.left
        #     root=stack.pop()
        #     res.append(root.val)
        #     root=root.right
        # return res
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
