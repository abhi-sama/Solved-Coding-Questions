'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the Binary Tree.
'''

# Binary tree node class for reference.
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None


# Functions to traverse on each part.
def isLeaf(root):
    if not root.left and not root.right:
        return True
def addLeftBoundary(root,res):
    cur=root.left
    while cur:
        if not isLeaf(cur):
            res.append(cur.data)
        if cur.left:
            cur=cur.left
        else:
            cur=cur.right        

def addBottomBoundary(root,res):
    if isLeaf(root):
        res.append(root.data)
        return
    if root.left:
        addBottomBoundary(root.left,res)
    if root.right:
        addBottomBoundary(root.right,res)

def addRightBoundary(root,res):
    cur=root.right
    temp=[]
    while cur:
        if not isLeaf(cur):
            temp.append(cur.data)
        if cur.right:
            cur=cur.right
        else:
            cur=cur.left 
    while temp:
        res.append(temp.pop())    
def traverseBoundary(root):
    res=[]
    if root==None:
        return res
    if not isLeaf(root):
        res.append(root.data)
    addLeftBoundary(root,res)
    addBottomBoundary(root,res)
    addRightBoundary(root,res)  
    return res
    pass