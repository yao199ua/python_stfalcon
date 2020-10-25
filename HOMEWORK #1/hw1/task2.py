# Розрахунок вартості сируНеобхідно створити таблицю вартості сиру вагою від 50 до 1000г.
# З кроком 50 г. Якщо ціна за 1 кг –х

def get_input_data(message):
    while True:
        try:
            value = input(message)
            return float(value)
        except:
            print('Please enter numeric value')

cheese_cost = get_input_data("Please, enter cheese cost per kg: ")

price_per_gramm = cheese_cost / 1000

for weight in range(50, 1050, 50):
    price = weight * price_per_gramm
    print("Weigth: {} \t Price: {}".format(weight, price))