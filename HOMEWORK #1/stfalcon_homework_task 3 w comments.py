# 3. Even & Odd numbers output
# тут має бути просто range(5, 16) - так як це в нас генератор значень, 
# однак результат запуску range не буде список у тому вигляді, якому ми його очікуємо отримати,
# елементи будуть створені під час виконання циклу, це зроблено для економії пам"яті
# замість check_numbers = [(range(5,16))]
check_numbers = range(5, 16)
even_numbers = []
odd_numbers = []

print(check_numbers)

# list(check_numbers) цю стрічку не треба

#even = 6,8,10,12,14
#odd = 5,7,9,11,13,15

for num in check_numbers:
    if num % 2 == 0:            #TypeError: unsupported operand type(s) for %: 'range' and 'int'
        # append - функція яка приймає параметром значення якке треба додати до списку
        #even_numbers.append() -> even_numbers.append(num)
        even_numbers.append(num)
    else:
        #odd_numbers.append() -> odd_numbers.append(num)
        odd_numbers.append(num)

print(even_numbers)
print(odd_numbers)