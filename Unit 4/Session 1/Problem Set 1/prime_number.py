"""
Write a function is_prime() that takes in a positive 
integer n and returns True if it is a prime number 
and False otherwise. A prime number is a number 
greater than 1 that has no positive divisors other 
than 1 and itself.

def is_prime(n):
    pass

Example Usage:

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))

Example Output:

True
False
False


input: integer
output: boolean representing whether the given integer is prime or not
rules: a number is prime when it is only divisible by 1 and itself

- check each number between 2 and (given number - 1) if the modulus
  of the given number with any of these numbers is 0 then the number
  is not prime
    - i.e. 10 modulus 2 is 0 so not prime

Algorithm
- iteate through the range of 2 to 1 less than the given number
    - if given number modulus current number is 0
        - return false
- return true
"""

def is_prime(n):
    for num in range(2, n):
        if n % num == 0:
            return False
        
    return True

print(is_prime(5))
print(is_prime(12))
print(is_prime(9))