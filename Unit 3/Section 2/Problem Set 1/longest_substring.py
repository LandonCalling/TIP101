"""
Write a function longest_uniform_substring() that takes 
in a string s and returns the length of the longest 
uniform substring. A uniform substring consists of a 
single repeated character.

def longest_uniform_substring(s):
    pass

Example Usage:

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)

Example Output:

4
1

input: string containing substrings of repeated chars
output: integer representing the longest substring
rules:
    - uniform substring consists of a single repeated char
    
Examples:
s1 = "aabbbbCdAA"
s2 = "abcdef"
s3 = "aabbccddaaaff"

data structure(s):

Algorithm:
- create current character variable and set equal to first 
  char in string and remove first char from string
- create counter variable to calculate length of substring
  and set equal to 1
- create list to contain substring lengths for comparison
  later
- iterate through string.  for each char
    - if it is the same as the current character variable
        - add one to the counter
    - otherwise
        - push counter to list
        - set current character to char
        - set counter to 1
- find max number in created list and return it
"""

def longest_uniform_substring(s):
    string_list = list(s)
    current_char = ""
    substring_length = 0
    all_substring_lengths = []
    
    for char in string_list:
        if char == current_char:
            substring_length += 1
        else:
            all_substring_lengths.append(substring_length)
            current_char = char
            substring_length = 1
    
    return max(all_substring_lengths)

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)