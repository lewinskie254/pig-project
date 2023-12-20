import random

def roll():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

while True: 
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 1 < players <= 4:
            break
        else:
            print("You can only choose a number between 2 and 4.")
    else:
        print("Invalid input. Provide a number")

max_score = 50
player_scores = [0 for _ in range(players)]

while True:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn has just started.")
        print(f"Your total Score is {player_scores[player_idx]}.\n")
        current_score = 0

        while True: 
            should_roll = input("Would you like to roll? (Y/N)")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1. You are done")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}.")
            
            print(f"Your current Score is {current_score}.")

        player_scores[player_idx] += current_score 

        print(f"Your total Score is {player_scores[player_idx]}.")
    
    max_score = max(player_scores)
    winning_idx = player_scores.index(max_score)

    print(f"player number {winning_idx + 1} wins with a score of {max_score}")