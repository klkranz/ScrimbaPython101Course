# It’s...not really an adventure game...#Ver 1.0
# The code should allow you to get 1 thing from each store and each item you get should be removed from the store
# inventory, then do same for next store... one way to buy is by typing the key 'newt' in an input box...or something.
# At the end you should print the 'items' you have taken...in this version you don't have to pay for stuff or add it up
# Ver 1.2
# add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistent item is
# bought(typed)
# Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total
# cost and how much gold you have left.
# TODO Ver 1.4
# random bug fix, 'browser compatibility', refactoring code..basically being lazy...stop scrolling TikTok/Facebook! ;-)
# TODO Ver 1.5
# print inventory before and after purchases as one department_store of stuff (combine inventories from all stores into
# one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find
# 'them'? Do you know why? May require knowledge of actual python 'lore'

purse = 1000
freelancers = {'name': 'Freelancing Shop', 'brian': 70, 'black knight': 20, 'biccus diccus': 100, 'grim reaper': 500,
               'minstrel': -15}
antiques = {'name': 'Antique Shop', 'french castle': 400,'german joke': 5, 'wooden grail': 3, 'scythe': 150,
            'catapult': 75}
pet_shop = {'name': 'Pet Shop', 'blue parrot': 10, 'white rabbit': 5, 'newt': 2}

print('Your village is being attacked by "a germanic tribe" and you need to run to each of the three stores and get ')
print('the right thing from each to save your village, and probably some good looking girl or boy you want to marry. ')
print('All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!')
print(f'You have {purse} Gp to make your purchases.')

cart = {}
bought_items = ''
for shop in (freelancers, antiques, pet_shop):
    print(f"Welcome to {shop['name']}!  You may \"exit\" the store if you do not want to purchase anything.")
    print(f"Today we have: ")
    for key, value in shop.items():
        if key == 'name':
            continue
        else:
            print(f"{key} costs {value}")
    buy_item = input(f"What do you want to buy?: ").lower()
    if buy_item == "exit":
        continue
    elif buy_item not in shop:
        print(f"The {shop['name']} does not have any {buy_item}. Please come again.")
        continue
    else:
        bought_items = bought_items + f': {buy_item} at {shop[buy_item]} Gp'
        cart.update({buy_item: shop.pop(buy_item)})
sum_purchases = sum(cart.values())
final_purse = purse - sum_purchases
print(f'You purchased{bought_items}. You spent {sum_purchases} Gp and have {final_purse} Gp remaining.')
print('Have a nice day of mayhem!')
if cart == {'minstrel': -15, 'german joke': 5, 'white rabbit': 5}:
    print("Congratulations! You found the best possible solution. You made money and defeated the enemy with ease!")
