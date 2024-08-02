import random
# this function will roll a dice
def roll_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

# here we get the number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4")
    else:
        print("Invalid input. Try again.")

#
max_score = 50
#players_scores = [0] * players or [0 for_ in range(players)]
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    for player_idx in range(players):
        print("\n Player number", player_idx + 1, "turn has started")
        print("your total score is", players_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll a dice? (y/n): ")
            if should_roll.lower() != "y":
                break
            
            value = roll_dice()
            if value == 1:
                print("You rolled a 1! Turn over!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a", value)
            
            print("Your score is", current_score)

        players_scores[player_idx] += current_score
        print("Your total score is", players_scores[player_idx])

max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("The winner is player number", winning_idx + 1, "with a score of", max_score)


