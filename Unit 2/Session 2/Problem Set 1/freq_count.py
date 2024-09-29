'''
Write a function that takes in a list of integers nums and 
counts the number of occurrences of each integer. The function 
returns the result as a dictionary with integers as keys and their counts as values.

def count_occurrences(nums):
    pass

Example Input: 
Example Output: {1: 1, 2: 2, 3: 3, 4: 1} 

- iterate through nums list
  - if output dictionary keys doesn't contain current num
    - add it to dict with a value 1
  - otherwise we add one to current value in dict
'''

def count_occurrences(nums):
    occurrences = {}
    for number in nums:
        if number not in occurrences.keys():
            occurrences[number] = 1
        else:
            occurrences[number] += 1
    
    return occurrences

nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))