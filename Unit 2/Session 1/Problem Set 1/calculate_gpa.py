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

Problem:
input: dictionary of type {"class":"letter grade"}
output: float representing the GPA for the report card, 
        2 places after the decimal point

Grade System as follows:
"A" = 4
"B" = 3
"C" = 2
"D" = 1
"F" = 0

Data Structure: Dict for containing conversion of letter grade to number value
 of type {"letter grade":number in range(5)}
 
Algorithm:
- create variable for containing the sum of all number grades
- iterate through the given dictionary
  - for a given item, convert the letter grade to number grade
    and add to sum
- divide sum by the number of grades in dictionary
- return average rounded to two decimal places
"""

def calculate_gpa(report_card):
    grade_sum = 0
    grade_conversion_table = {"A" : 4, "B" : 3, "C" : 2, "D" : 1, "F": 0}
    
    for grade in report_card.values():
        grade_sum += grade_conversion_table[grade]
    
    GPA = grade_sum / len(report_card)
    
    return "{:.2f}".format(GPA)

report_card = {"Math": "A", 
               "Science": "C", 
               "History": "A", 
               "Art": "B", 
               "English": "B", 
               "Spanish": "A"}
               
print(calculate_gpa(report_card))