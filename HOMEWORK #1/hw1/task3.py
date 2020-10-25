# Виведення парних танепарних чисел
# Написати програму для виведення парних та непарних чисел на проміжку від n до m

def get_input_data(message):
    while True:
        try:
            value = input(message)
            return int(value)
        except:
            print('Please enter numeric value')

begin_interval = get_input_data("Please enter start value of interval: ")
end_interval = get_input_data("Please enter end value of interval: ")

if begin_interval > end_interval:
    tmp = begin_interval
    begin_interval = end_interval
    end_interval = tmp

even_list = []
odd_list = []

for number in range(begin_interval, end_interval + 1):
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)

print('even numbers', even_list)
print('odd numbers', odd_list)