my_set = {1, 3, 4}

my_dict = {'name': 'Jose', 'age': 23, 'grades': [13, 45, 53, 6]}
print(my_dict)

lottery_player = [
{
    'name': 'Rolf', # for this  key
    'numbers': (13, 45, 66, 23, 22) # tuples as the values
},
{
    'name': 'John', # for this  key
    'numbers': (14, 56, 80, 22, 22) # tuples as the values
}
]
universities = [
    {
        'name': 'Oxford',
        'location': 'UK'
    },
    {
        'name': 'MIT',
        'location': 'US'
    }
]

# calculate the total of numbers the lottery_player

print("suma lottery_player ", sum(lottery_player['numbers']))

# changing the key value

lottery_player['name'] = 'John'
print(lottery_player)

# simplify
sum(lottery_player["numbers"])
#
lottery_player[0].total()

lottery_player.total()

