"""
Given the head of a linked list and a value val, 
return the frequency of val in the list. Evaluate 
the time and space complexity of your solution. 
Define your variables and provide a rationale for 
why you believe your solution has the stated time 
and space complexity.

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def count_element(head, val):
	pass

Example Usage:

# Input List: 3 -> 1 -> 2 -> 1
# Input: head = 3, val = 1

Example Output:

# 2

Inputs:
  - Node: Contains an integer and a pointer to the next Node
  - integer to find frequency of.
Outputs:
  - Integer representing the frequency of the given number
    in the linked list
Rules:
  - Evaluate time and space complexity of solution
  - Define variables and provide rationale for why
    solution has the stated complexity

Find the frequency of a given value in the provided linked list.

Plan:
  - create pointer (current_node) to keep track of where in the list we are
  - create variable (frequency) to count occurences of given value
  - iterate through given linked list. For each Node:
    - if current node value is the same as the given value
        - add one to frequency count
    - move to next Node in list
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def count_element(head, val):
    frequency = 0
    current_node = head
    
    while current_node:
        if current_node.value == val:
            frequency += 1
        current_node = current_node.next
    
    return frequency

head = Node(3, Node(1, Node(2, Node(1))))
print(count_element(head, 1))

"""
Time and Space Complexity
----------------------------
Time: O(n)
  - The important part here is the while loop.
  - Block inside the while loop is O(1) because
    each of the operations inside is O(1).
  - The while loop itself will always run through 
    the entire list.  Since the linked list is provided
    to the function as an input, the while loop
    will run as many times as there are items in the
    linked list.  Therefore the while loop has O(n)
    complexity, making the complexity of the
    entire function O(n).
Space Complexity: O(1)
  - No complex data structures are created inside of the function.
  - All of the variables created have O(1) space complexity.
  - Therefore the function has O(1) space complexity.

"""