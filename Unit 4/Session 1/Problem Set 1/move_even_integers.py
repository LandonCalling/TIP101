"""
Write a function sort_list_by_parity() that takes 
in an integer list nums as a parameter and moves 
all the even integers at the beginning of the list 
followed by all the odd integers. The function returns 
any list that satisfies this condition.

def sort_array_by_parity(nums):
    pass

Example Usage:

nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))

Example Output:

[2,4,3,1]
# Additional acceptable outputs are [4,2,3,1], [2,4,1,3], and [4,2,1,3]
[0]

- create two empty lists, one for even nums and one for odd
- iterate through the given list
    - if even add to even list
    - otherwise add to odd list
"""

def sort_list_by_parity(nums):
    even_list = []
    odd_list = []
    
    for num in nums:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    
    return even_list + odd_list


nums = [3,1,2,4]
nums2 = [0]
print(sort_list_by_parity(nums))
print(sort_list_by_parity(nums2))

