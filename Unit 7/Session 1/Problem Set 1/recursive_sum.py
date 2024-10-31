"""
Without using the built-in sum() function, 
write a function sum_list() that calculates 
the sum of all values in a list recursively.

What is the time complexity of this function? What is the space complexity?

def sum_list(lst):
	pass

Example Usage:

# Example Input: [1, 2, 3, 4, 5]

Example Output:

# Expected Output: 15
# Explanation: 1 + 2 + 3 + 4 + 5 = 15

S: elem at index 0 + sum_list(the rest of the array slice 1:)
base case: length of the array is 1 return element at position 0
"""


def sum_list(lst):
    if len(lst) == 1: 
        return lst[0]
    else:
        return lst[0] + sum_list(lst[1:])
    
print(sum_list([1, 2, 3, 4, 5]))