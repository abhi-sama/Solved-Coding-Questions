#User function Template for python3


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def left(root,level,res):
    if root is None:
        return 
    if level==len(res):
        res.append(root.data)
    left(root.left,level+1,res)
    left(root.right,level+1,res)
def LeftView(root):
    res=[]
    left(root,0,res)
    return res
