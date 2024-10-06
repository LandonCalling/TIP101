"""
Write a function reverse_only_letters() that takes 
in a string s as a parameter. The function reverses 
the order of the letters in the string and returns 
the new string. Non-letter characters should remain 
in their original positions.

def reverse_only_letters(s):
    pass

Example Usage:

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)

Example Output: j-Ih-gfE-dCba

input: string containing both alpha and non_alpha chars
output: string with alpha chars reversed, and non_alpha chars in same place
rules:
    - case should be preserved

Algorithm:
- convert string into list of chars
- create list of chars in string remove non-alpha chars
    - create mepty list
    - iterate through given string.  for each char
        - if char is an alpha, add to end of list
- swap chars
    - iterate through first half of list.  for each char
        - swap current position with position -(cur pos + 1),
- insert non-alpha chars back into string
    - iterate through string.  for each char
        - if char is not alpha
            - insert into list at current position
- join list back into string and return
"""

def reverse_only_letters(s):
    string_list = []
    
    for char in s:
        if char.isalpha():
            string_list.append(char)
    
    half_length = len(string_list) // 2
    
    for index in range(half_length):
        string_list[index], string_list[-(index + 1)] = \
        string_list[-(index + 1)], string_list[index]
    
    for idx, char in enumerate(s):
        if not(char.isalpha()):
            string_list.insert(idx, char)
    
    return "".join(string_list)

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)