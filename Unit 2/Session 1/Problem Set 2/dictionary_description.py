"""
The following function get_description() takes in a dictionary 
info and a list keys as parameters. For each key in keys, the 
function prints the value associated with that key in info and 
prints None if the key does not exist in info.

However, the function has a bug! Copy the function into your 
Replit and run the code. Work with your group members to find 
the cause of the bug and correctly implement the function.

def get_description(info, keys):
    for key in keys:
	    print(info[key])
    
   
info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)

"""