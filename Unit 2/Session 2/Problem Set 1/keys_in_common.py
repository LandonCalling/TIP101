
'''
Write a function that takes in two dictionaries, dict1 and dict2 
and finds all keys common to both dictionaries. The function returns a list of common keys.

def common_keys(dict1, dict2):
	pass

Example Usage:

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)

Example Output:

['b', 'c']

input: is two dictionaries of the form "a": 1
output: list of common keys between the two

Plan:
-create common_list to contain common keys between dict1 and dict2
- iterate through list of keys from dict1
  - if the current key is contained in dict 2
    - add to common_list
- return common_list
'''

def common_keys(dict1, dict2):
    common_list = []
    
    for key in dict1.keys():
        if key in dict2.keys():
            common_list.append(key)
    
    return common_list

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)