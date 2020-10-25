# 1. % Calculation
'''
deposit_start = 500
# Initial deposit amount
interest_rate = 0.05
# % increase rate
income = deposit_start * interest_rate
# yearly income
deposit_years = [1,2,3,4,5]
# deposit duration
'''

'''
def deposit_fin():
  #  for deposit_duration in
# input('Введіть суму вкладу')
    
    return income
'''

#print(type(deposit_years)) #list\array?

'''
def deposit_final(deposit_start,deposit_years):
    for year in deposit_years:
        deposit_start + income
        return deposit_final
        year =+1

deposit_final(deposit_start,deposit_years)

print (deposit_final(500,5))
'''

'''
def deposit_fin(deposit_start,deposit_rate,deposit_years):
    deposit_start = 500
    interest_rate = 0.05
    deposit_years = [1,2,3,4,5] # what if we don't know when the deposit ends?
    income = deposit_start * interest_rate
    for year in deposit_years:
        deposit_fin = deposit_start*deposit_rate+deposit_start
    year += 1
        
    print(deposit_fin)
'''
def get_input_data(message):
    while True:
        try:
            value  = input(message)
            value = float(value)
        except: 
            print('Please enter a numeric value: ')

deposit = get_input_data('Enter deposit amount: ')
percent = get_input_data('Enter percent: ')
duration = get_input_data('Enter duration: ')

converted_percent = percent / 100

for i in range(duration):
    profit = deposit*converted_percent
    print(profit)