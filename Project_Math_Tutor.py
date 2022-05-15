# Math Tutor Project : Create application to practice multiplication tables.
# 1. User specifies the number off random practice questions.
# 2. User is presented with a prompt e.g. 5 X 5 = and inputs the answer for each of the questions.
# 3. When all questions are answered, print out the following info:
#    a. Some form of thanks for playing greeting.
#    b. Number of correct answers/total answers.
#    c. Percentage correct.
# Bonus 1: Measure/present the time it took to answer questions, in total and per question.
# Bonus 2: Let user specify how high the numbers should be.
# Bonus 3: Show all questions and answers at end.
from random import randint

def math_tutor(questions, highest):
    recap = ["Here is a recap of the questions you answered:"]
    score = 0
    for n in range(0, questions):
        num1 = randint(1, highest)
        num2 = randint(1, highest)
        correct_ans = num1 * num2
        user_ans = int(input(f"Question {n + 1}: What is {num1} X {num2}? "))
        recap.append(f"Question {n + 1}: {num1} X {num2} = {correct_ans}. You answered {user_ans}.")
        if correct_ans == user_ans:
            score += 1
    print("Thank you for practicing math with me!")
    print(f"You answered {score} out of {questions} questions correctly.")
    print(f"If this had been a test you would have earned a {score / questions * 100}%.")
    return print("\n".join(recap))

num_questions = int(input("Welcome! How many questions would you like to have today? "))
highest_number = int(input("What is the highest number you would like to practice today? "))
math_tutor(num_questions, highest_number)
