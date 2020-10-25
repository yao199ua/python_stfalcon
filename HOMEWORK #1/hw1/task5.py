#Скласти програму для обчислення суми цифр цілого числа і їх кількості.

def get_input_data(message):
    while True:
        try:
            value = input(message)
            return int(value)
        except:
            print('Please enter numeric value')

number = get_input_data("Please, enter number: ")

number_length = len(str(number))
print("Count of chars: ", number_length)

sum = 0
divide = 1
for n in range(number_length):
    value = int(number / divide % 10)
    sum += value
    divide *= 10
print("Sum: ", sum)