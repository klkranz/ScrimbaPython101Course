names = ['john ClEEse', 'Eric IDLE', 'michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']
# msg = "You are invited to the party on Saturday."  # Alternative way would be to have a variable for the basic
# message which would make it easier to change for the next party.
new_list = names + names1
# names += names1  # cleaner way to do this unless you wanted to preserve the original lists.
# names.extend(names1)  # alternative way to add the two lists.
# With either of these two, you would then use names below instead of new_list as the variable in the loops.
for new in range(2):
    new_list.append(input("Provide the name of another person to be invited: "))
    # names.append(input("Enter a new name: "))

for name in new_list:
    print(f"{name.title()}! You are invited to the party on Saturday.")
    # msg1 = f"{name.title()}! {msg}"
    # print(msg1)
