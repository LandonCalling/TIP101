"""
Write a function calculate_gpa() that calculates the grade point 
average (GPA) for a student based on their course grades and 
returns the gpa as a float. The function takes in a dictionary 
report_card as a parameter where each key-value pair represents a 
course and the grade received in that course respectively. 
The grades are represented as strings ("A", "B", "C", "D", "F") 
and each grade corresponds to a certain number of grade points:

"A" = 4
"B" = 3
"C" = 2
"D" = 1
"F" = 0

A GPA is calculated by finding the average of all grade points.

def calculate_gpa(report_card):
    pass

Example Usage:

report_card = {"Math": "A", 
               "Science": "C", 
               "History": "A", 
               "Art": "B", 
               "English": "B", 
               "Spanish": "A"}
               
print(calculate_gpa(report_card))

Example Output: 3.33
"""