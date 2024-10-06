"""
Write a function sum_of_unique_elements() that 
takes in two lists of integers, lst1 and lst2, 
as parameters and returns the sum of the elements 
that are unique in lst1.

An element is unique if:

    it appears exactly once in lst1
    it does not appear in lst2

def sum_of_unique_elements(lst1, lst2):
	pass

Example Usage:

lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)

sum2 = sum_of_unique_elements(lstC, lstB)
print(sum2)

Example Output

3
0

Given two lists, calculate the sum of all unique values in the first list.

input: 2 lists of integers
output: the sum of all unique values in the first list
rules: a value is unique if it doesn't appear in the second list
       and only appears in the first list once

Algorithm:
- create a dict with values from first list as keys and their
  frequencies as values
    - create empty dictionary freq_dict
    - iterate through first list
        - if the current element is a key in freq_dict
            - add one to the value contained by that key
        - otherwise
            - create a new entry in freq_dict with the 
              current element as the key, and 1 as the 
              value
- from this dictionary make a list of values that appear in the
  the first list only once
    - create empty list uniq_values
    - iterate through freq_dict
        - if the value for the current key is 1
            - append key to the end of uniq_values
- remove values in created list that appear in list two
    - iterate through a copy of uniq_list
        - if the current element is contained in list two
            - remove from uniq_list
- return sum of all values in created list
"""

def sum_of_unique_elements(lst1, lst2):
    freq_dict = {}

    for num in lst1:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1

    uniq_values = [key for key in freq_dict if freq_dict[key] == 1]

    for num in uniq_values.copy():
        if num in lst2:
            uniq_values.remove(num)

    sum = 0

    for num in uniq_values:
        sum += num

    return sum

lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

print(sum_of_unique_elements(lstA, lstB))
print(sum_of_unique_elements(lstC, lstB))