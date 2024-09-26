"""
Imagine you are working on a book review software like Goodreads. 
Write a function named highest_rated() that returns the book with 
the highest rating.

The function should take in a list of dictionaries named books as 
a parameter. Each dictionary represents data associated with a book, 
including its title, author, and rating. The function should return 
the dictionary for the book with the highest rating.

def highest_rated(books):
    pass

Example Input:

books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

Expected Output:

{"title": "A Fortune For Your Disaster",
 "author": "Hanif Abdurraqib",
 "rating": 4.47
}


Problem:
Given a list of books, find the book with the highest rating.

- input: list of books
- output: dictionary representing highest rated book
- each dictionary is of the form 
    - {"title": "Title",
       "author": "Author",
       "rating": range(?)}

Examples:
books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

Expected Output:

{"title": "A Fortune For Your Disaster",
 "author": "Hanif Abdurraqib",
 "rating": 4.47
}

Algorithm:
- remove the first dict(book) from the list
  and save as the highest rating. 
- iterate through the remaining list of books 
  comparing each book's rating with the previous
  rating.
    - if the rating is greater, save as highest rating
- return highest rating

"""

def highest_rated(books):
    highest_rated_book = books[0]
    books = books[1:]
    
    for book in books:
        if book["rating"] > highest_rated_book["rating"]:
            highest_rated_book = book
    
    return highest_rated_book
    
books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

print(highest_rated(books))