"""
Given the root of a binary tree, return a list 
representing the inorder traversal of its nodes' 
values. In an inorder traversal we traverse the 
left subtree, then the current node, then the 
right subtree.

class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def inorder_traversal(root):
	pass

Example Usage:

Example Input Tree #1: 
     1
      \
       2
      / 
     3    

Input: root = 1
Expected Output: [1,3,2]

Example Input Tree #2 : 

Input: root = None
Output: []

Example Input Tree #3:
    1  

Input: root = 1
Output: [1]

Algorithm:
  - Base Case: left and right child nodes for current node are None
    - push value for current node to result array
  - does the left node exist? call function on left node
  - push value for current node to result array
  - does the right node exist? call function on right node
  
"""
class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def inorder_traversal(root, result):
    if root is None:
        pass
    elif root.left or root.right:
        if root.left:
            inorder_traversal(root.left, result)
        result.append(root.val)
        if root.right:
            inorder_traversal(root.right, result)
    else:
        result.append(root.val)

    return result

root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
result=[]
print(inorder_traversal(root, result))

root = None
result = []
print(inorder_traversal(root, result))

root = TreeNode(1)
result = []
print(inorder_traversal(root, result))