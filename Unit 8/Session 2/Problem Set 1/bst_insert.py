"""
Given the root of a binary search tree, 
insert a new node with a given key and 
value into the tree. Return the root of 
the modified tree. The tree is sorted by key. 
If a node with the given key already exists, 
update the the existing key’s value. You do 
not need to maintain a balanced tree.

Evaluate the time complexity of your function.

class TreeNode():
     def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.val = value
            self.left = left
            self.right = right
   
def insert(root, key, value):
	pass

Example Usage:

Example Input Tree #1: (tree depicted using keys)

      10
     /  \
    /    \
   5      15
  / \    
 1   6    

Input: root = 10, key = 9, value = 'Naruto' 
Expected Output: root = 10
Expected Output Tree:

      10
     /  \
    /    \
   5      15
  / \    
 1   6
      \
       9    


Example Input Tree #2: Empty Tree (None)

Input: root = None, key = 4, value = "Sailor Moon"
Expected Output: root = 4
Expected Output Tree:


base case:
    - root is null return new node containing the key/value pair
    - if key less than root key root.left = recursive call to left child
    - if key is greater than root key root.right = recursive call to the right child
    - return root
"""

class TreeNode():
     def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.val = value
            self.left = left
            self.right = right
   
def insert(root, key, value):
    if root:
      if key < root.key:
         root.left = insert(root.left, key, value)
      elif key > root.key:
         root.right = insert(root.right, key, value)
    else:
        root = TreeNode(key, value)

    return root

def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.key, root.val)
        print_tree(root.right)


Node10 = TreeNode(10, "Bears")
Node5 = TreeNode(5, "Lions")
Node15 = TreeNode(15, "Dolphins")
Node1 = TreeNode(1, "Sharks")
Node6 = TreeNode(6, "Cubs")
Node10.left = Node5
Node10.right = Node15
Node5.left = Node1
Node5.right = Node6
root = Node10

root = insert(root, 9, "Naruto")
print_tree(root)

root = None
root = insert(root, 4, "Sailor Moon")
print_tree(root)