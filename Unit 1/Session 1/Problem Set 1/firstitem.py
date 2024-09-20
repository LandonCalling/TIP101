"""
Write a function 'get_first()' that tkaes in a list as a parameter and returns the first item in the list.
Return 'None' if the list is empty.

input: list
output: None or the first item in the list

Examples:
[] - None
[3, 1, 6, 7, 5] - 3
[4] - 4

Algorithm:
- If the list is empty return None
- Otherwise return first element
"""

def get_first(list):
    if len(list) == 0:
        return None
    else:
        return list[0]

print(get_first([]))
print(get_first([4]))
print(get_first([3, 1, 7, 5]))