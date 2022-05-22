print("Welcome, to NetworkChuck Coffee!!")
name = input("What is your name?\n").title()
if name == "Ben" or name == "Patricia" or name == "Loki":
    evil = input("Are you evil?\n").lower()
    good_deeds = int(input("How many good deeds have you done today?\n"))
    if evil == "yes" and good_deeds < 4:
        print(f"Get out of here, {name}. You are not welcome here.")
        exit()
else:
    evil = "no"
if evil != "yes":
    beard = float(input("How long is your beard in inches?\n"))
    if beard >= 1:
        print(f"We support bearded people such as you, {name}, so please move to the front of the line.")
    else:
        print(f"Thank you for coming, {name}. Please wait in the line to the counter.\n\n")
menu = "Black Coffee, Espresso, Latte, Cappuccino and Frappuccino."
print("Today our menu is: " + menu)
order = input(f"What can I get for you today, {name}?\n").title()

if order == "Frappuccino":
    price = 13
elif order == "Black Coffee":
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    whipped_cream = input("Would you like extra whipped cream on that?\n").lower()
    if whipped_cream == yes:
        price = 11
    else:
        price = 9
elif order == "Cappuccino":
    price = 10
else:
    print(f"I'm sorry. We don't have any {order} on our menu. Please move the back of the line\n"
          f"while you review the menu and come back when you are ready to order.\n"
          f"We have {menu}")
    exit()
quantity = int(input(f"How many {order}s would you like?\n"))
bill = quantity * price
if quantity > 1:
    order += "s"
print(f"Thank you, {name}. Your {quantity} {order} comes to ${bill}, and will be ready in a few moments.")
