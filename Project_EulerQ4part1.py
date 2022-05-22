# Project Euler #4 - Program that shows the largest palindrome created by multiplication of two 3-digit numbers
# a palindrome is a number that is the same backwards and forwards, like 101 or 990099
import time

# Define a function that tests if a given input is a palindrome
#def is_palindrome(test_data):
#    test_string = str(test_data)
#    for i in range(0,len(test_string)//2):
#        if test_string[i] != test_string[-(i + 1)]:
#            return False
#        else: continue
#    return True
# I like his better
def is_palindrome(val):
    return str(val) == str(val)[::-1]
# Create a loop to generate numbers to test if they are palindromes
start_time = time.time()
palindromes = []
iteration = 0
for n in range(100, 1000):
    for x in range(100, 1000):
        iteration += 1
        test_num = n * x
        if is_palindrome(test_num):
            palindromes.append((f"{n} X {x} =", test_num))

print(palindromes)
print(max(palindromes, key=lambda item: item[1]))
print(f"# of iterations: {iteration}")
print(f"Time taken: {time.time() - start_time}")

def is_palindrome(val):
    return str(val) == str(val)[::-1]

# Function created after seeing his solution
def palindrome(low_val, high_val):
    start_time = time.time()
    palindromes = []
    iterations = 0
    for num_a in range(high_val, low_val - 1, -1):
        for num_b in range(high_val, low_val - 1, -1):
            iterations += 1
            test_num = num_a * num_b
            if is_palindrome(test_num):
                palindromes.append((f"{num_a} X {num_b} =", test_num))
    print(palindromes)
    print(max(palindromes, key=lambda item: item[1]))
    print(f"# of iterations: {iterations}")
    print(f"Time taken: {time.time() - start_time}")


palindrome(100, 999)

# Look at it from another point of view. What if we create a list of all permutations of palindromes between
# 998,001 (999 * 999) and 10000 (100 * 100). Then see if each palindrome is divisible by two 3-digit numbers.
