#Iterative Approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr=root

        while curr:
            if curr.val<p.val and curr.val<q.val:
                curr=curr.right
            elif curr.val>p.val and curr.val>q.val:
                curr=curr.left
            else:
                return curr
        
        return

# TC=O(h)
# SC=O(1)
        

#Recursive Approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        
        if root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root

# TC=O(h)
# SC=O(h)
        