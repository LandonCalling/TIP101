"""
In the game League of Legends, Teemo attacks his 
enemy Ashe with poison arrows. Write a function 
find_poisoned_duration() that takes in two parameters: 
time_series (the time at which Teemo's attacks hits 
Ashe) and time_duration (the duration of the poisoning 
effect). The function returns the total time that Ashe 
is in a poisoned condition.

time_series is a list of integers that represents the 
times at which Teemo attacks and makes Ashe poisoned 
for the exact time_duration.

If Teemo hits Ashe while she is still poisoned, the 
poison's duration starts over. For example, if Teemo 
attacks at times 1 and 4 for 3 seconds, the states at 
each time would be:

1: attacked
2: in poison state
3: in poison state
4: attacked, poison duration resets to 3
5: in poison state
6: in poison state
7: in poison state 
8: in normal state

This means that the total time that Ashe is in a poisoned condition is 5.

def find_poisoned_duration(time_series, duration):
    pass

Example Usage:

time_series = [1,4,9]
damage = find_poisoned_duration(time_series, 3)
print(damage)

Example Output: 8

input:
    - list representing the times ash is attacked
    - integer representing the poison duration in seconds
output: integer representing the total seconds ash was poisoned
rules: an attack doesn't count as poison second even if it
       otherwise would have been

Examples:
time_series = [1,4,9]
damage = find_poisoned_duration(time_series, 3)
print(damage)

Example Output: 8

time_series = [1,4]
damage = find_poisoned_duration(time_series, 3)
print(damage)

Example Output: 5


"""