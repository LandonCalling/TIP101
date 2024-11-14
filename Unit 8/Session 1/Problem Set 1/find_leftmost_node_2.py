"""
If you implemented the previous left_most() function iteratively, implement it recursively. If you implemented it recursively, implement it iteratively.

Evaluate the time complexity of the function.

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
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    current_node = root
    
    if current_node:
        while current_node.left:
            current_node = current_node.left
        
        return current_node.val
    
    return None

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
print(left_most(root))
root = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(left_most(root))
root = None
print(left_most(root))