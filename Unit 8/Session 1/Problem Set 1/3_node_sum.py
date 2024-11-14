"""
Given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child, return True if the value of the root is equal to the sum of the values of its two children. Return False otherwise.

Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
	pass

Example Usage:

Example Input Tree #1: 
  10
 /  \
4    6
Input: root = 10
Expected Output: True

Example Input Tree #2: 
  5
 / \
3   1
Input: root = 5
Expected Output: False
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
	return root.left.val + root.right.val == root.val

root = TreeNode(10, TreeNode(4), TreeNode(6))
print(check_tree(root))
root = TreeNode(5, TreeNode(3), TreeNode(1))
print(check_tree(root))
