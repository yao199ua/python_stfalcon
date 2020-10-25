# 3. Even & Odd numbers output
check_numbers = [(range(5,16))]
even_numbers = []
odd_numbers = []

print(check_numbers)

list(check_numbers)

#even = 6,8,10,12,14
#odd = 5,7,9,11,13,15

for num in check_numbers:
    if num % 2 == 0:            #TypeError: unsupported operand type(s) for %: 'range' and 'int'
        even_numbers.append()
    else:
        odd_numbers.append()

print(even_numbers)
print(odd_numbers)