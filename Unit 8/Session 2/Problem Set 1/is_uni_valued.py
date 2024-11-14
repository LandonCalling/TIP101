"""
A binary tree is uni-valued if every node in 
the tree has the same value. Given the root of 
a binary tree, return True if the given tree is 
uni-valued and False otherwise.

Evaluate the time complexity of your solution.

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def is_univalued(root):
	pass

Example Usage:

Example Input Tree #1

      1
     / \
    /   \
   1     1
  / \     \
 1   1     1

Input: root = 1
Expected Output: True

Example Input Tree #2

      1
     / \
    /   \
   1     2
  / \     \
 1   1     1

Input: root = 1
Expected Output: False

univalued - all nodes in tree contain same value
base case:  current node has no children
subproblem: sub tree is univalued
relationship: current node and subtree(s) have same value
"""

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def is_univalued(root):
    if root.left is None and root.right is None:
        return True
    elif (root.left and not root.right) and (root.left.val == root.val):
        return True and is_univalued(root.left)
    elif (root.right and not root.left) and (root.right.val == root.val):
        return True and is_univalued(root.right)
    elif root.right.val == root.val and root.left.val == root.val:
        return True and is_univalued(root.left) and is_univalued(root.right)
    else:
        return False

Node1 = TreeNode(1)
Node2 = TreeNode(1)
Node3 = TreeNode(1)
Node4 = TreeNode(1)
Node5 = TreeNode(1)
Node6 = TreeNode(1)
Node1.left = Node2
Node1.right = Node3
Node2.left = Node4
Node2.right = Node5
Node3.right = Node6
print(is_univalued(Node1))

Node1 = TreeNode(1)
Node2 = TreeNode(1)
Node3 = TreeNode(2)
Node4 = TreeNode(1)
Node5 = TreeNode(1)
Node6 = TreeNode(1)
Node1.left = Node2
Node1.right = Node3
Node2.left = Node4
Node2.right = Node5
Node3.right = Node6
print(is_univalued(Node1))