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
def marble_draw(mode, user_bet):
    if mode == "hard":
        bag = ("black", "green", "green", "green", "green", "green", "red", "red", "red", "white")
    else:
        bag = ("green", "green", "green", "green", "green", "green", "red", "red", "red", "red")
    marble = random.choice(bag)
    if marble == "green":
        result = user_bet
    elif marble == "black":
        result = user_bet * 10
    elif marble == "white":
        result = -user_bet * 5
    else:
        result = -user_bet
    return marble, result

# Bonus - give the user the option to play in hard mode.
print("Let's play a little betting game. Each round a marble will be pulled from a bag and either add or subtract\n"
      "from the amount of gold coins in your purse. In standard mode, there are 6 green marbles and 4 red marbles.\n"
      "Green marbles add the amount you bet to your purse, and red marbles subtract the amount you bet from your \n"
      "purse.  In hard mode, 1 black marble replaces a green but adds 10X what you bet to your purse, and 1 white\n"
      "marble replaces a red marble but subtracts 5X what you bet from your purse. Ready to play?")
game_mode = input("What game mode would you like to play? standard or hard: ").lower()
start_purse = int(input("What would you like your starting purse to be (just hit enter to play with 1000): ") or "1000")
rounds = int(input("How many rounds would you like to play (just hit enter to play a random number of rounds: ")
             or random.randrange(3,51))

# Create "purse" which will start at 1000 and change with each bet/draw round.
purse = start_purse
# Create a loop for a random number of rounds.
for n in range(0, rounds):
    bet = int(input(f"For round {n + 1}, you have {purse} gold pieces in your purse. "
                    f"How much would you like to bet this round? "))
    draw, results = marble_draw(game_mode, bet)
    # Print results of each round.
    print(f"This round a {draw} marble was pulled and added {results} to your gold pieces.")
    # Add/Subtract amount designated by the marble from the user's purse.
    purse += results
    # Break the loop if purse drops below 500.
    if purse <= 0.5 * start_purse:
        print("Game Over - You lost over half of your gold pieces.")
        break

# At the end of the loop, they win if the purse is > 1000, break even if = 1000 and lose if < 1000.
if purse > 1000:
    print(f"Congratulations, you won with {purse} gold pieces.  You gained {purse - 1000} gold today!")
elif purse == 1000:
    print(f"You broke even today. You didn't gain or lose anything, but hopefully you enjoyed the time spent.")
else:
    print(f"Unfortunately, you lost {1000 - purse} gold pieces. Hopefully, you still had fun in the game.")
print("Thank you for playing. If you had fun, please come play again.")
