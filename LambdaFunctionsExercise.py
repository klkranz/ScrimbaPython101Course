# Turn the following function into a lambda function instead.

def f(x): return x + 5


print(f(2))

# My version (note his version assigned the lambda function to the variable f)
print((lambda x: x + 5)(2))


def strip_spaces(str):
    return ''.join(str.split(' '))


print(strip_spaces('Monty Pythons Flying Circus'))

# My version
print((lambda str: ''.join(str.split(' ')))('Monty Pythons Flying circus'))


def join_list_no_duplicates(lista, listb):
    return list(set(lista + listb))


list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6, 7]
print(join_list_no_duplicates(list_a, list_b))

# My version
print((lambda a, b: list(set(a + b)))(list_a, list_b))


# Complete the function so it returns a function
def create_quad_func(a, b, c):
    # return function f(x) = ax^2 + bx + c
    return lambda x: a * x ** 2 + b * x + c


f = create_quad_func(2, 4, 6)
g = create_quad_func(3, 4, 5)
print(f(2))
print(g(2))

signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
print(sorted(signups))  # Lexicographic sort (first by the letters than by the first number seen).
# write sorting by integer
print(sorted(signups, key=lambda id: int(id[3:])))  # Integer sort


# Exercise: Sort this by score using lambda!
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = sorted([Eric, John, Terry], key=lambda person: person.score)
print([player.name for player in player_list])

# Alternate version based on how he did it.
player_list.sort(key=lambda gamer: gamer.score)
print('Lowest to highest:', [player.name for player in player_list])
player_list.sort(key=lambda person: person.score, reverse=True)
print('Highest to lowest:', [player.name for player in player_list])
