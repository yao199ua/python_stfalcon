print('hello')

a = 1 + 2

if a == 3:
    print('true')

arr = range(1,4)
for i in arr:
    print(i) # 1 2 3

arr2 = [[1.1, 1.2], [2.1,2.2], [3.1, 3.2, 3.2]]

for i in arr2:
    for j in i: 
        print(j)
    print('')

#i usually reserved for rows
#j usually reserved for columns
#k usually reserved for 3rd dimension


car = {'brand':'kia', 'fuel':'gas', 'year':'1900'}
#
car2 = {'brand':'skoda', 'fuel':'diesel', 'year':'1910'}

print(car) #{'brand': 'kia', 'fuel': 'gas', 'year': '1900'}
print(car2) #{'brand': 'skoda', 'fuel': 'diesel', 'year': '1910'}

cars = [{'brand':'kia', 'fuel':'gas', 'year':'1900', 'multimedia': {'acoustics':8, 'touchscreen':True, 'led':False}}, 
{'brand':'skoda', 'fuel':'diesel', 'year':'1910', 'model':'octavia'},
dict(brand = 'opel', fuel = 'gas', year = 2001)] #another way to create a dictionary, just like above

print(cars) # [{'brand': 'kia', 'fuel': 'gas', 'year': '1900', 'multimedia': {'acoustics': 8, 'touchscreen': True, 'led': False}}, {'brand': 'skoda', 'fuel': 'diesel', 'year': '1910', 'model': 'octavia'}, {'brand': 'opel', 'fuel': 'gas', 'year': 2001}]

print(cars[0])  # {'brand': 'kia', 'fuel': 'gas', 'year': '1900'}

print(cars[1]['fuel'])  # diesel

print(cars[1].get('model')) #None allows to ignore error if a key is missing

for car in cars: #iteration per car
    print(car) 
    #{'brand': 'kia', 'fuel': 'gas', 'year': '1900'}
    #{'brand': 'skoda', 'fuel': 'diesel', 'year': '1910', 'model': 'octavia'}
    
    for value in car.values(): #unpacks values from dictionary.
        print(value)
        #skoda
        #diesel
        #1910
        #octavia

cars[0]['fuel'] = 'diesel' #call a key or value and change it
print(cars)

for car in cars:
    car['year'] = 2000

print(cars) # changed every year value to 2000

print(len(cars[0])) #3

objectlength = len(cars[0])
print(objectlength) #3 also but a bit more readable


car3 = {'brand':'kia', 'fuel':'gas', 'year':'1900'}
del car3['fuel']
print(car3) #{'brand': 'kia', 'year': '1900'} < fuel is now absent.

del cars[1]
print('')   # empty space
print(cars) #Skoda is now deleted


car = cars[0]
print(car['multimedia']) # {'acoustics': 8, 'touchscreen': True, 'Led': False}
print(car['multimedia']['led']) #False


obj_type = type(cars[1])
print(cars[1]) # {'brand': 'opel', 'fuel': 'gas', 'year': 2000}
print(obj_type) # <class 'dict'>


def print_hello():
    print('hello world')

print_hello() #hello world


class Car:
    def __init__(self, brand, year): #функція-конструктор яка може зініціалізувати певні значення
        self.brand = brand
        self.year = year
        self.model = 'octavia'

#!!!!!  self.  вказує про те, що значення цих змінних будуть доступні всюди в  класі.

    def set_year(self,year): # функція буде оновлювати рік ств. машини
        self.year = year 

    def car_info(self):
        print(self.brand, self.model, self.year)

car = Car('kia', 1999)
car.car_info() # kia octavia 1999

car.set_year(2001)
car.car_info() # kia octavia 2001

car = Car('kia', 1999)
car2 = Car('open',2001)

cars = [car, car2]

carDict = {'brand':'skoda','year':2002}

print(cars) 
# [<__main__.Car object at 0x00000272C9E22CD0>, <__main__.Car object at 0x00000272C9E22880>]
print (cars[0].car_info()) # kia octavia 1999
#None
print(cars[0].year)     #1999
print(carDict['year'])  #2002
print(cars[1].brand)    #open

class Shoes:
    brand = 'reebok'
    size = 41
    season = 'winter'



name = input('Valerii, please enter your name: ')

if name == 'Bill' or name == 'Steve':
    print('Hi Bill') #Hi Bill
elif name == 'Kate' and name == 'Valerii':
    print('Greetings, ' +name)
else:
    print('hey, ' +name)

# !!!! Ternary Operator: it's like if, else but in a single line:
# Can't use it together with elif
#Тернарний оператор має лише 2 можливих варанти розвитку подій

output_message = 'hello Bill' if name == 'Bill' else 'hello ' +name
print(output_message) #hello Bill



def get_input():
    counter = 10
    while counter > 0:
        number = input('Enter the number: ')
        try:
            return int(number)
        except:
            print('please enter a number. Attempts left: {}'.format(counter))
            print('test')
        finally: 
            counter -= 1

number = get_input()

arr = [1,2,3,4,5]

if number in arr:
    print('{0} found'.format(number)) #3 found
else:
    print('not found') # when 10 attempts are depleted > not found



vehicles = [{ 'model':'renault', 'year':2077},
{'model':'peugeout'}]

key = 'year'
for vehicle in vehicles:
    if 'year' in vehicle:
        print(vehicle['year']) 
#2077
    if 'model' in vehicle:
       pass
#renault
#peugeout
       print(vehicle.get(key)) #None


transports = ['car','moto','plane',1,2,3,4,5]
print(transports[1:-1:2]) # ['moto', 1, 3]


def get_data():
    return (1, 'test','234')

output = get_data()
print(output) #(1, 'test', '234')

'''output[1] = 1111
print(output[1])''' # Error: tuples are immutable.


import math
sum = math.pi * 2
print(sum)

string = '6.283185307179586'
print(len(string)) #17

import random
print(random.randint(0,4))  #0 or any other in range.
print(random.choice([1,2,3,4,5,6,'x'])) # < gets back any random element of a list
print(random.randrange(1,100))


str = 'hello world'
str = 'd' + str[1:]
print(str) #dello world

#перетворення стрічки в список
word = list(str)
print(word)

for i in str:
    print(i)


words = ['i', 'drive', 'a', 'car']
sentence = ' '.join(words) #space is used a divider here. Good to use with tags
 # i drive a car

words[0] = 'Everyday'
sentence = ' '.join(words)
print(sentence) # Everyday drive a car
# напряму в стріічці не можна передодати символ, але це можна зробити через список


updated = str.find('world')
print(updated) # 6 returns index of what you were looking for
#if not found > will return -1

updated2 = str.replace('world','universe')
print(updated2)  # dello universe

upd3 = str.split('r')
print(upd3) # ['dello wo', 'ld']

words.sort()
print(words) # ['Everyday', 'a', 'car', 'drive']
words.reverse()
print(words) # ['drive', 'car', 'a', 'Everyday']


test_tup = ('apple', 'kiwi', 'banana')
print(test_tup[0]) # apple IMMUTABLE

test_arr = ['apple', 'kiwi', 'banana']
print(test_arr[0]) # apple MUTABLE

# test_tup[0] = 'cola' WRONG!!! Tuple object does not support item assignment

tmp = list(test_tup)
tmp[0] = 'cola'
test_tup = tuple(tmp)
print(test_tup) # ('cola', 'kiwi', 'banana')

#Tuple with 1 elemet = element + ,
test_tuple = ('apple',)
print(type(test_tuple)) # <class 'tuple'>

test_array = ['apple']
print(type(test_array)) # <class 'list'>
print(test_array) # ['apple'] <<< we don't this comma for lists, only for tuples

tuple3 = test_tup + test_tuple
print(tuple3) # ('cola', 'kiwi', 'banana', 'apple')

print(tuple3.count('apple')) # 1

