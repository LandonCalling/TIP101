"""
Write a function remove_duplicates() that takes 
in a sorted list of integers nums as a parameter 
and removes all duplicates in the list. The 
function returns the modified list.

def remove_duplicates(nums):
    pass

Example Input: nums = [1,1,1,2,3,4,4,5,6,6]
Example Output: no_dups = [1,2,3,4,5,6]

input: list of integers containing duplicates
output: list of unique integers

"""

def remove_duplicates(nums):
    no_dups = [nums.pop(0)]
    
    for num in nums:
        if num not in no_dups:
            no_dups.append(num)
    
    return no_dups

nums = [1,1,1,2,3,4,4,5,6,6]
no_duplicates = remove_duplicates(nums)
print(no_duplicates)