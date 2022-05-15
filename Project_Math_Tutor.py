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
from time import time

def math_tutor(questions, highest):
    recap = ["Here is a recap of the questions you answered:"]
    score = 0
    all_start = time()
    for n in range(0, questions):
        num1 = randint(1, highest)
        num2 = randint(1, highest)
        correct_ans = num1 * num2
        q_start = time()
        user_ans = int(input(f"Question {n + 1}: What is {num1} X {num2}? "))
        q_end = time()
        recap.append(f"Question {n + 1}: {num1} X {num2} = {correct_ans}. You answered {user_ans} in "
                     f"{round(q_end - q_start,1)} seconds.")
        if correct_ans == user_ans:
            score += 1
    all_end = time()
    print("Thank you for practicing math with me!")
    print(f"You answered {score} out of {questions} questions correctly in {round(all_end - all_start,1)} seconds.")
    print(f"If this had been a test you would have earned a {round(score / questions * 100)}%.")
    return print("\n".join(recap))

num_questions = int(input("Welcome! How many questions would you like to have today? "))
highest_number = int(input("What is the highest number you would like to practice today? "))
math_tutor(num_questions, highest_number)

# His program:
## import modules
#from  random import randrange as r
#from time import time as t
## ask how many questions user wants
#no_questions = int(input('How many questions do you want?: '))
#max_num =int(input('Highest number used in practice?: '))
##set score start at zero
#score = 0
#answer_list = []
##loop through number of questions
#start = t()
#for q in range(no_questions):
#    num1,num2 = r(1,max_num+1),r(1,max_num+1)
#    ans = num1 * num2
#    u_ans =int(input(f'{num1} X {num2} = '))
#    answer_list.append(f'{num1} X {num2} = {ans} you:{u_ans}')
#    if u_ans == ans:
#        score += 1
#    end = t()
#print(f'Thank you for playing! \nYou got {score} out of {no_questions} ({round(score/no_questions*100)}%) correct in
#      {round(end-start,1)} seconds ({round((end-start)/no_questions,1)}seconds/question)')
#for a in answer_list:
#    print(a)
## create two random numbers and calc answer
## show user the question
## capture answer and modify user score
## output final score

