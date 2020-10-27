def get_input_data(message):
    while True:
        try:
            value  = input(message)
            #value = float(value)
            #тут має бути return
            return float(value)
        except: 
            print('Please enter a numeric value: ')

deposit = get_input_data('Enter deposit amount: ')
percent = get_input_data('Enter percent: ')
duration = get_input_data('Enter duration: ')

converted_percent = percent / 100

for i in range(int(duration)):
    profit = deposit*converted_percent
    deposit += profit
    print('Year: {} \t amount: {:.2f}'.format(i+1, deposit))

