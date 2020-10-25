# Розрахунок відсотківНа скільки відсотків зросте депозитний вклад у банку через n років, якщо річний приріст складає x%.
# Інтервал нарахування один раз на рік.
# Input data:
#     •Сума вкладу(500)
#     •Відсоткова ставка річна(5)
#     •Тривалість депозиту(n)5

def get_input_data(message):
    while True:
        try:
            value = input(message)
            return float(value)
        except:
            print('Please enter numeric value')

deposit = get_input_data("Enter deposit amount: ")
percent = get_input_data("Enter percent: ")
duration = get_input_data("Enter duration: ")

converted_percent = percent / 100

for i in range(int(duration)):
    profit = deposit * converted_percent
    deposit += profit
    print("Year: {} \t amount: {:.2f}".format(i + 1, deposit))