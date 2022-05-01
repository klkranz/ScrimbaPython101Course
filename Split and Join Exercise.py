# From the list given, fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
print(csv)
csv = ",".join(csv.split(":"))
print(csv)
csv = ",".join(csv.split(";"))
print(csv)
friends_list = csv.split(",")
print(friends_list)

# same principle, but nesting the commands.
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)

# Another way to do it.
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
print('replace', csv.replace(';',',').replace(':',',').split(','))