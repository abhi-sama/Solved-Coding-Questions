#Iterative Approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[]
        q.append(root)
        current=root
        res=[]
        if root==None:
            return res
        while q:
            levelSize=len(q)
            temp=[]
            for i in range(levelSize):
                ele=q.pop(0)
                temp.append(ele.val)
                if ele.left!=None:
                    q.append(ele.left)
                if ele.right!=None:
                    q.append(ele.right)
            res.append(temp)

        return res

# TC=O(n)
# SC=O(n)
            
#Recursive Approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]

        def dfs(node,level):
            if not node:
                return None
            if len(res)==level:
                res.append([])
            res[level].append(node.val)
            dfs(node.left,level+1)
            dfs(node.right,level+1)
        dfs(root,0)
        return res

# TC=O(n)
# SC=O(n)
            