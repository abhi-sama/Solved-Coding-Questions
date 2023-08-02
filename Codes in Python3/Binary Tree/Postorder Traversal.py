# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        s=[]
        cur=root
        while cur or s:
            if cur:
                s.append(cur)
                cur=cur.left
            else:
                temp=s[-1].right
                if temp is None:
                    temp=s.pop()
                    res.append(temp.val)
                    while s and temp==s[-1].right:
                        temp=s.pop()
                        res.append(temp.val)
                else:
                    cur=temp
        return res
        # s1=[]
        # s2=[]
        # res=[]
        # if root is None:
        #     return res
        # s1.append(root)
        # while s1 :
        #     temp=s1.pop()
        #     res.append(temp.val)
        #     if temp.left :
        #         s1.append(temp.left)
        #     if temp.right:
        #         s1.append(temp.right)
        # # while s2 :
        # #     temp=s2.pop()
        # #     res.append(temp.val)
        # return res[::-1]