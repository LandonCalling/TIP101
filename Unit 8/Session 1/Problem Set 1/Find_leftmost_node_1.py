"""
Given the root of a binary tree, write a function 
that finds the value of the left most node in the tree.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
	pass

Example Usage:


Example Input Tree #1: 

      1
     / \
    /   \
   2     5
  / \    
 4   3    

Input: root = 1
Expected Output: 4

Example Input Tree #2: 

     1
      \
       2
      / 
     3    

Input: root = 1
Expected Output: 1

Example Input Tree #3: 

Input: root = None
Output: None


Plan:
- Base Case: next left node is none return current value
- Relationship: return left_most(next left node)

"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if root is None:
        return None
    elif root.left is None:
        return root.val
    else:
        return left_most(root.left)

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
print(left_most(root))
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(left_most(root))
root = None
print(left_most(root))
