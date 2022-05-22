# Hey, we're going on a camping trip!!
# Make a list with variable camp_stuff = all the supplies.
camping_list = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive",
              "beard oil", "marshmallows"]
camp_site = ["Crystal Lake", 404, 89.3, True]

#camping_list.remove("tent")
#camping_list.remove("sleeping bags")
camping_list.pop(0)
#camping_list.append("toilet paper")
#camping_list.append("bidet")
# OR
#camping_list.extend(["toilet paper", "bidet"])
# OR
#camping_list += ["toilet paper", "bidet"]
# To tell it where to add the items
camping_list.insert(-1, "toilet paper")
camping_list.insert(0, "bidet")

network_chuck = [camping_list[0], camping_list[5], camping_list[-3]]
me = [camping_list[3], camping_list[6], camping_list[-2], camping_list[-1]]
print(f"The list of stuff needed are {camping_list}.")
print(f"Network Chuck is bringing the {', '.join(network_chuck)} and I am bringing {', '.join(me)}.")
