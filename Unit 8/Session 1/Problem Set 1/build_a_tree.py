"""
Given the following TreeNode class, create the binary 
tree depicted in the image below.

Binary Tree Example:
    10
   /  \
  4    6

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(10, TreeNode(4), TreeNode(6))