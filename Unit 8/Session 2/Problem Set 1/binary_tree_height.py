"""
Given the root of a binary tree, write 
a function height() that returns the 
height of a binary tree.

Evaluate the time complexity of your function.

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
   
def height(root):
	pass

Example Usage:

Example Input Tree #1

      4
     / \
    /   \
   2     5
  / \    
 1   3    

Input: root = 4
Expected Output: 3

Example Input Tree #2 

      4 

Input: root = 4
Expected Output: 1


base case: current node is null return 0
subproblem: height of subtree
relationship: 1 + height of largest subtree
"""

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
   
def height(root):
    if root:
        left_height = 0
        right_height = 0
        if root.left:
            left_height = height(root.left)
        if root.right:
            right_height = height(root.right)
        
        return 1 + (left_height if left_height > right_height else right_height)
    else:
        return 0

Node4 = TreeNode(4)
Node2 = TreeNode(2)
Node5 = TreeNode(5)
Node1 = TreeNode(1)
Node3 = TreeNode(3)

Node4.left = Node2
Node4.right = Node5
Node2.left = Node1
Node2.right = Node3
print(height(Node4))

Node4 = TreeNode(4)
print(height(Node4))