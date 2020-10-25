# Написати програму, яка б запитувала скорочене ім’я і друкувала повне для 5 друзів. 
# Для незнайомих писати «Я з вами не знайома»

friends = {
    'Mark': 'Full Mark',
    'Bill': 'Test Bill',
    'Ryan': 'O Ryan',
    'Taras': 'Taras Shevchenko',
    'Alex': 'Alex Mack',
}

name = input('Please, enter the name: ')

if name in friends:
    print(friends[name])
else:
    print('Sorry, I don\'t know you!')