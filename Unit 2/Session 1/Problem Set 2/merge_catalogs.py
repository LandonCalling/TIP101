"""
Write a function merge_catalogs() that combines two product catalogs, 
catalog1 and catalog2 as parameters. Each parameter is a dictionary 
where each key-value pair represents a product name and its price, 
respectively. If the same product exists in both catalogs, the price 
from the second catalog should overwrite the price in the first. 
Return the updated first catalog dictionary.

def merge_catalogs(catalog1, catalog2):
    pass

Example Input:

catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}

Example Output: {"apple": 1.0, "banana": 0.75, "cherry": 1.25}
"""