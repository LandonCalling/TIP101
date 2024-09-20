"""
Write a function quality_control() that takes in a dictionary 
product_scores and an integer threshold as parameters. The 
dictionary product_scores has key-value pairs that represent 
a product ID and its quality rating.

If the product has a score greater than or equal to threshold, 
the function categorizes it as a "pass".

If the product has a score less than threshold, the function 
categorizes it as a "fail".

The function returns a new dictionary where the key-value pair 
is the product ID and whether it is a "pass" or "fail".

def quality_control(product_scores, threshold):
    pass

Example Input:

scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
threshold: 60

Example Output: {"x0123": "pass", "x0124": "fail", "x0125": "pass", "x0126": "fail"}
"""