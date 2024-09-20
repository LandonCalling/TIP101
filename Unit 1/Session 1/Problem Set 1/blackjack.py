"""
Write a function call 'blackjack()' that takes an integer 'score' as a parameter, and prints out a statement
based on the following rules:
score greater than 21 - "Bust!"
score equal to 21 - "Blackjack!"
score >= 17 and < 21 - "Nice hand!"
score less than 17 - "Hit me!"

input: integer
output: none

Examples:
blackjack(24) # --> "Bust!"
blackjack(19) # --> "Nice hand!"
blackjack(21) # --> "Blackjack!"
blackjack(10) # --> "Hit me!"

Algorithm:
Print statment to screen based on score input to function.
"""

def blackjack(score):
    if score > 21:
        print("Bust!")
    elif score == 21:
        print("Blackjack!")
    elif score >= 17 and score < 21:
        print("Nice hand!")
    else:
        print("Hit me!")
        
blackjack(24) # --> "Bust!"
blackjack(19) # --> "Nice hand!"
blackjack(21) # --> "Blackjack!"
blackjack(10) # --> "Hit me!"