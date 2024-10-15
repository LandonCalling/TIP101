"""
The reverse_list() problem can also be solved without 
using the two pointer technique (as you may have seen 
it in previous units)! Evaluate the time and space 
complexity of your two-pointer solution.

Then, evaluate the time and space of the following solution:

def reverse_list(lst):
    # Create a new reversed list
    reversed_lst = lst[::-1] O(1)
    # Copy the elements back into the original list
    for i in range(len(lst)): * n
        lst[i] = reversed_lst[i] O(1)

O(n)

Which has better time complexity?
Which has better space complexity?

def reverse_list(lst):
    left =0  O(1)
    right = len(lst)-1 O(1)

    while right > left: n
        lst[right], lst[left] = lst[left], lst[right] O(1)
        left += 1 O(1)
        right -= 1 O(1)

O(n)
"""