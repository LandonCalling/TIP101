"""
Write a function is_subsequence() that takes in a list of integers lst 
and a list of integers sequence as parameters. Given these two lists, 
determine whether the sequence list is a subsequence of the lst list. 
A subsequence of a list is a set of numbers that aren't necessarily 
adjacent but are in the same relative order as they appear in the list. 
Return True if sequence is a subsequence, and False otherwise.

def is_subsequence(lst, sequence):
    pass

Example Usage:

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))

Example Output: True

- create index for traversal of list
- iterate through sequence checking for matches
    - if we get to the end of the list while searching
        - return false
    - compare current seq elem to elem of lst at index
        - if same add 1 to index, 
- return true
"""

def is_subsequence(lst, sequence):
    index = 0
    
    for number in sequence:
        while index < len(lst):
            if number != lst[index]:
                index = index + 1
            else:
                break
        if index >= len(lst):
            return False
        
    return True
    

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, 10, -1]
print(is_subsequence(lst, sequence))