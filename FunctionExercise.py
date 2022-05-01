# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps
# 6. Favorite color should be in lowercase

def greeting(name="friend", age=28, color="red"):
    # Greets the user with their name and age on their next birthday, and defaults to 28 if not specified.
    print(f"Hello, {name.capitalize()}! You will be {age + 1} on your next birthday.")
    # Mentions the favorite color given and defaults to red if not specified.
    print(f"We hear you like the color {color.lower()}!")


user_name = input("Enter your name: ")
user_age = int(input("Enter your current age: "))
fav_color = input("Enter your favorite color: ")
greeting(name=user_name, age=user_age, color=fav_color)
greeting(color="PINK")
greeting("Tiffany")
greeting()
