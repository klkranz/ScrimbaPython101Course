# It’s...not really an adventure game...#Ver 1.0
# Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to
# save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl.
# VAT... chop chop!! ze germanz are coming!
# The code should allow you to get 1 thing from each store and each item you get should be removed from the store
# inventory, then do same for next store... one way to buy is by typing the key 'newt' in an input box...or something.
# At the end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
# TODO Ver 1.2
# add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistent item is
# bought(typed)
# Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total
# cost and how much gold you have left.
# TODO Ver 1.4
# random bug fix, 'browser compatibility', refactoring code..basically being lazy..stop scrolling TikTok/Facebook! ;-)
# TODO Ver 1.5
# print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into
# one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find
# 'them'? Do you know why? May require knowledge of actual python 'lore'

# create stores
freelancers = {'name': 'freelancing Shop', 'brian': 70, 'black knight': 20, 'biccus diccus': 100, 'grim reaper': 500,
               'minstrel': -15}
antiques = {'name': 'Antique Shop', 'french castle': 400, 'wooden grail': 3, 'scythe': 150, 'catapult': 75,
            'german joke': 5}
pet_shop = {'name': 'Pet Shop', 'blue parrot': 10, 'white rabbit': 5, 'newt': 2}

# create an empty shopping cart
cart = {}
# loop through stores/dicts
for shop in (freelancers, antiques, pet_shop):
    # input box to show what you can buy...capture text string of what was bought...make lowercase
    print(f"Welcome to {shop['name']}!")
    print(f"Today we have: ")
    for key, value in shop.items():
        if key == 'name':
            continue
        else:
            print(f"{key} costs {value}")
    buy_item = input(f"What do you want to buy?: ").lower()
    # update the cart
    cart.update({buy_item: shop.pop(buy_item)})
    bought_items = ", ".join(list(cart.keys()))
print(f'You Purchased {bought_items}. Today it is all free. Have a nice day of mayhem!')
