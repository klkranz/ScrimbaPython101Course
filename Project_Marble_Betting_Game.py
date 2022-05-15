# Project: Trading Game Simulation - Create a marble betting game:
# Draw a marble from a bag (assume it's random).
# The bag has 10 marbles: 6 Green and 4 Red.
#    If the user draws a Green marble, the user wins the same amount that the user bet.
#    If the user draws a Red marble, the user loses the amount that the user bet.
#    Bonus: Replace two marbles.
#       1 Green becomes 1 Black which is worth 10X the user's' bet (winning that amount).
#       1 Red becomes 1 White worth 5X the user's bet (losing that amount).
# Marbles are placed back in the bag after each round so the odds stay the same each round.
# User starts with 1000 gold pieces (or other currency) and before each round the user inputs the amount they will bet.
# The number of rounds/draws should be variable.
# The game ends with a loss immediately, if the user loses half their money.
# Show the user how they are doing at each draw, so they know how they are doing.

# Import random module.
import random

# Create a function that pulls a random marble from the bag of marbles.
def marble_draw(mode):
    if mode == "hard":
        bag = ["black", "green", "green", "green", "green", "green", "red", "red", "red", "white"]
    else:
        bag = ["green", "green", "green", "green", "green", "green", "red", "red", "red", "red"]
    return random.choice(bag)

# Bonus - give the user the option to play in hard mode.
game_mode = input("What game mode would you like to play? standard or hard: ").lower()

# Create "purse" which will start at 1000 and change with each bet/draw round.
purse = 1000
# Create a loop for a random number of rounds.
for n in range(0, random.randrange(3,10)):
    bet = int(input(f"For round {n + 1}, you have {purse} gold pieces in your purse. "
                    f"How much would you like to bet this round? "))
    marble = marble_draw(game_mode)
    if marble == "green":
        purse += bet
        print(f"You drew a {marble} marble and won {bet} gold pieces.")
    elif marble == "black":
        purse += bet * 10
        print(f"You drew a {marble} marble and won {bet * 10} gold pieces.")
    elif marble == "white":
        purse -= bet * 5
        print(f"You drew a {marble} marble and lost {bet * 5} gold pieces.")
    else:
        purse -= bet
        print(f"You drew a {marble} marble and lost {bet} gold pieces.")
    # Break the loop if purse drops below 500.
    if purse <= 500:
        break
    # Print results of each round.

# At the end of the loop, they win if the purse is > 1000, break even if = 1000 and lose if < 1000.
if purse > 1000:
    print(f"Congratulations, you won with {purse} gold pieces.  You gained {purse - 1000} gold today!")
elif purse == 1000:
    print(f"You broke even today. You didn't gain or lose anything, but hopefully you enjoyed the time spent.")
else:
    print(f"Unfortunately, you lost {1000 - purse} gold pieces. Hopefully, you still had fun in the game.")
print("Thank you for playing. If you had fun, please come play again.")
