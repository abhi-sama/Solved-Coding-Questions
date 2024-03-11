# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[]
        result=[]
        if root is None:
            return result
        q.append(root)
        leftToRight=True
        while q:
            size=len(q)
            level=[0]*size
            for i in range(size):
                node=q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                index = i if leftToRight==True else size-1-i
                level[index] = node.val         
            leftToRight= not leftToRight
            result.append(level)
        return result
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res = []
#         if not root:
#             return res
#         q = deque()
#         leftToRight = True
#         q.append(root)
        
#         while q:
#             qLen = len(q)
            
#             temp = []
            
#             for i in range(qLen):
#                 node = q.popleft()
#                 if node:
#                     if leftToRight:
#                         temp = temp + [node.val]
#                     else:
#                         temp = [node.val] + temp
#                     q.append(node.left)
#                     q.append(node.right)
#             leftToRight = not leftToRight
#             if temp:
#                 res.append(temp)
#         return res

        