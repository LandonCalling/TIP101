"""
Given the root of a binary tree, print the value of each node in the tree.

You can print the values in any order, on the same line or on separate lines.

Just print the values and don't make it look like a tree or anything fancy like that.

Ex: root is the node with value 50:
            50
        /       \ 
     30          70
    /  \        /   \  
  20    40     60   80 
 / \   / \    /  \
10    35         65

print_tree(root) # outputs 10, 20, 30, 35, 40, 50, 60, 65, 70, 80 (Any order is fine)
"""


### SETUP CODE: do not change ###
class TreeNode:

   def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right


node10 = TreeNode(10)
node20 = TreeNode(20)
node30 = TreeNode(30)
node35 = TreeNode(35)
node40 = TreeNode(40)
node50 = TreeNode(50)
node60 = TreeNode(60)
node65 = TreeNode(65)
node70 = TreeNode(70)
node80 = TreeNode(80)
node50.left = node30
node50.right = node70
node30.left = node20
node30.right = node40
node20.left = node10
node40.left = node35
node70.left = node60
node70.right = node80
node60.right = node65

root = node50

### WRITE YOUR FUNCTION HERE ####


def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val)
        print_tree(root.right)
print_tree(root)
print_tree(None)