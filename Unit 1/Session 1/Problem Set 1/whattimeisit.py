"""
    Write a function that takes an integer 'hour' as a parameter.
    If 'hour' is  2, the function should return "taco time 🌮"
    IF 'hour' is 12, the function should return "peanut butter jelly time 🥪"
    Otherwise, the function should return "nap time 😴"

    Input: integer, representing hours
    Output: string

    Examples:
    time = what_time_is_it(2)
    print(time) --> "taco time"
    time = what_time_is_it(7)
    print(time) --> "nap time"
    time = what_time_is_it(12)
    print(time) --> "peanut butter jelly time"

    Algorithm:
    create variable time_string
    set variable to approriate string based on integer input
    return variable
"""


def what_time_is_it(hour):
    if hour == 2:
        time_string = "taco time 🌮"
    elif hour == 12:
        time_string = "peanut butter jelly time 🥪"
    else:
        time_string = "nap time 😴"
    
    return time_string

time = what_time_is_it(2)
print(time) # --> "taco time"
time = what_time_is_it(7)
print(time) # --> "nap time"
time = what_time_is_it(12)
print(time) # --> "peanut butter jelly time"