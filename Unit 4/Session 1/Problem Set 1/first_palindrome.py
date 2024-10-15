"""
Write a function first_palindrome() that takes 
in a list of strings words as a parameter and 
returns the first palindromic string in the list. 
A string is palindromic if it reads the same 
forward and backward. If there is no such string, 
return an empty string ""

def first_palindrome(words):
    pass

Example Usage:

words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)

Example Output:

ada
racecar
''

input: list of strings
output: first palindrom in list as a string
rules: if no palindromes return empty string 
       palindrome is the same forward and backward
       
Algorithm:
- iterate through list of words
    - is the word a palindrome?
        return word
- return empty string

- break string into list of chars
- set two pointers one to the beginning of the list
  one to the end of the list
- while the right pointer is larger than the left
    - if the two chars at left and right pointer are not equal
        - return false
- return true
"""

# This function has O(n) time complexity
def is_palindrome(string):
    chars = list(string)
    left = 0
    right = len(chars) - 1
    
    while right > left:
        if chars[left] != chars[right]:
            return False
        else:
            left += 1
            right -= 1
    return True

# This function has O(n^2) time complexity
def first_palindrome(words):
    for word in words:
        if is_palindrome(word):
            return word

    return ''


words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)