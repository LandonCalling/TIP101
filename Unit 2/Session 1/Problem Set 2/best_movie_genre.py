"""
Imagine you're contributing to a move recommendation engine, and 
you're tasked with writing a function named most_popular_genre() 
that returns the genre with the highest average rating across all 
movies.

The function takes in a list of dictionaries named movies as a 
parameter. Each dictionary represents data associated with a movie, 
including its title, genre, and rating. The function calculates the 
average rating for each genre and returns the genre with the highest 
average rating.

def most_popular_genre(movies):
    pass

Example Usage:

movies = [
    {"title": "Inception",
     "genre": "Science Fiction",
     "rating": 8.8
    },
    {"title": "The Matrix", 
     "genre": "Science Fiction",
     "rating": 8.7
    },
    {"title": "Pride and Prejudice", 
     "genre": "Romance",
     "rating": 7.8
    },
    {"title": "Sense and Sensibility", 
     "genre": "Romance",
     "rating": 7.7
    }
]

print(most_popular_genre(movies))

Example Output: Science Fiction

"""