# 2. Cheese price calculation
'''
cheese_mass = [(range(50,1001,50))]

print(cheese_mass)

print((range(50,1001,50))

# cheese_mass = list(range(50,1001,50)) # SyntaxError: invalid syntax

cheese_mass = list[(range(50,1001,50))] # SyntaxError: invalid syntax

for g in cheese_mass:    #g stands for grams
    cheese_price = g / 2
    
cheese_price = cheese_mass / 2

#how to get a single INT value from a list??
'''
'''
def get_input_data(message):
    while True:
        try:
            value = input(message)
            return float(value)
        except:
            print('Please enter numeric value')

cheese_cost = get_input_data("Please, enter cheese cost per kg: ")

price_per_gramm = float(cheese_cost) / 1000

for weight in range(50, 1001, 50):
    price = weight * price_per_gramm
    print("Weight: {} \t Price: {:.2f}".format(weight, price))
'''

def get_input_data(message):
    while True:
        try:
            value = input(message)
            return float(value)
        except:
            print('Please enter a numeric value')

cheese_cost = get_input_data('Please enter cheese cost per kg: ')

price_per_gramm = cheese_cost / 1000

for weight in range(50,1001,50):
    price = weight * price_per_gramm
    print('Weight: {} \t Price: {:.2f}'.format(weight, price))