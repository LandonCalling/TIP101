"""
You're developing an analytics tool for a sports league. Your task 
is to write a function named team_with_best_average_score() that 
returns the team with the highest average score over a season.

The function should accept a list of dictionaries named games as a 
parameter. Each dictionary represents data from a game, including 
the "team_name", and the "score" they achieved in that game. The 
function calculates the average score for each team across all games 
and returns the team with the highest average score.

def team_with_best_average_score(games):
    pass

Example Usage:

games = [
    {"team_name": "Lions",
     "score": 23
    },
    {"team_name": "Tigers", 
     "score": 30
    },
    {"team_name": "Lions", 
     "score": 27
    },
    {"team_name": "Bears", 
     "score": 20
    },
    {"team_name": "Tigers", 
     "score": 24
    },
    {"team_name": "Bears", 
     "score": 22
    }
]

print(team_with_best_average_score(games))

Example Output: Tigers
"""