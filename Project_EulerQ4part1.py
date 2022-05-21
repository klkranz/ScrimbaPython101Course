# Project Euler #4 - Program that shows the largest palindrome created by multiplication of two 3-digit numbers
# a palindrome is a number that is the same backwards and forwards, like 101 or 990099

# Define a function that tests if a given input is a palindrome
def is_palindrome(test_data):
    test_string = str(test_data)
    for i in range(0,len(test_string)//2):
        if test_string[i] != test_string[-(i + 1)]:
            return False
        else: continue
    return True

# Create a loop to generate numbers to test if they are palindromes
palindromes = []
for n in range(100, 1000):
    for x in range(100, 1000):
        test_num = n * x
        if is_palindrome(test_num):
            palindromes.append((f"{n} X {x} =", test_num))

print(palindromes)
print(max(palindromes, key=lambda item: item[1]))
