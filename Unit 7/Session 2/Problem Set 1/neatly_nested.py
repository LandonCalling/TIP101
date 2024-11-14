"""
Subproblem/Relationship first and last character off the string
                        and is_nested(substring)
Base Case(s) Empty Sting

Relationship First/last pair AND is_nested(substring)

"(())"

True
- if empty string 
    - return true
- remove the first and last characters
    - check to see if they form a pair
        - call function on what remains
    - return false
"""

def is_nested(paren_s):
    if not paren_s:
        return True
    
    if paren_s[0] == '(' and paren_s[-1] == ')':
        return is_nested(paren_s[1:-1])
    else:
        return False
    
print(is_nested("(())"))
print(is_nested("(()"))