"""
Write a function is_long_pressed() that takes in a string 'name' 
and a string 'typed' as parameters. Imagine your friend is typing 
their name into a keyboard and when typing a character, the key 
might get long pressed and the character will be typed 1 or more times.

The function should examine the typed characters and return 'True' 
if it is possible that it was your friends name with some characters 
being long pressed and False otherwise.

Use the two-pointer approach to solve the problem, which is a common 
technique in which we initialize two variables (also called a pointer 
in this context) to track different indices or places in a list or 
string, then moves the pointers to point at new indices based on
certain conditions. A common variation of this technique is to point
one variable at the beginning of one string and a second pointer at 
the beginning of a second string, then increment each pointer 
conditionally to solve a problem.

def is_long_pressed(name, typed):
    pass

Example Usage:

name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))

name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))

name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))

Example Output:

# 'a' and 'e' were long pressed in "alex"
True
# there are two 'e's in "saeed", and only one 'e' in the typed string 
False
# equal strings are considered long pressed

input: two strings, name and typed
output: boolean representing whether the typed string is a possible
        match to the name string
rules:
    - typed must be a match for name with possible long presses of
      repeated chars in typed
    - the freqency of each letter in typed must meet or exceed the
      frequency of each letter in name

Examples:
name = "alex"
typed = "aaleex"

name:   a l e x
point1: |
typed:  a a l e e x
point2: |

0, 0) letters match
    - set current letter in typed as previous letter
    - increment both pointers

name:   a l e x
point1:   |
typed:  a a l e e x
point2:   |

1, 1) letters don't match, typed matches previous letter
    - increment point2
    
name:   a l e x
point1:   |
typed:  a a l e e x
point2:     |

1, 2) letters match
    - set typed letter as previous letter
    - increment both pointers

possible outcomes of comparison
    - letter in typed matches letter in name
    - letter in typed doesn't match letter in name
        - letter in typed matches previous letter in type
        - letter in typed doesn't match previous letter in type

name2 = "saeed"
typed2 = "ssaaedd"



"""