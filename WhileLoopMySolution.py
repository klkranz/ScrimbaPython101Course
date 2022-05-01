print('Guessing game')
print("Guess a number. If you guess correctly within 3 guesses, you win.")
guesses = 3
while guesses > 0:
    user_guess = int(input(f"You have {guesses} left. Please enter a number between 1 and 10: "))
    if user_guess == 6:
        print("You have won the guessing game!")
        break
    else:
        guesses -= 1
        if guesses == 0:
            print("You have lost the game. Please play again.")

print("Let's try a different one. Guess a number betwee 1 and 100.")
guesses = 5
while guesses > 0:
    user_guess = int(input(f"You have {guesses} left. Please enter a number between 1 and 10: "))
    if user_guess == 42:
        print("You have won the guessing game!")
        break
    elif user_guess > 42:
        print(f"Your guess of {user_guess} is too high. Try again.")
        guesses -= 1
        if guesses == 0:
            print("You have lost the game. Please play again.")
        else:
            continue
    else:
        print(f"Your guess of {user_guess} is too low. Try again.")
        guesses -= 1
        if guesses == 0:
            print("You have lost the game. Please play again.")
        else:
            continue
