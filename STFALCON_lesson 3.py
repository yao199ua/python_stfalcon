'''
def reciprocal(num):
    try:
        r = 1/num
    except:
        print('Exception caught')
        return
    return r

print(reciprocal(10))
#0.1

print(reciprocal(0))
#Exception caught
#None

b = 1
c = None
try:
    if b == 0:
        raise ZeroDivisionError('cannot divide 0')
    c = 3/b

    print('hello python')
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
finally: # is always executed no matter what errors appear above
    print('finally')

print('Hello World')
print(c)
'''
###########################################################################################################

a_list = ['a','b','c','d', 3, 5]

#print(namez[2])
'''
counter = 0
for i in names:
    counter += 1
    print(counter)
    print(i)

name_1 = ['hello','world','python']

counter = 0
for name in name_1:
    if name == 'world':
        print('found')
'''
names = ['hello','world','python', 'hello','world','python']

counter = 0
for name in names:
    if name == 'world':
        counter +=1

print('world count is: ')
print(counter)
##########################################################################################################
import math # option 1
from math import cos

res = math.cos(3)
print(res)

res2 = cos(3) # option 2
print(res2)

###############################################################################################################

#Global Variables

gvar = 10
def printValue():
    print(gvar)

def updateValue():
    global gvar #allows to access the global variable
    gvar = 15

printValue()
updateValue()
printValue()

################################################################################################################
# in

inputValue = 'abc'
arr = [1,2,3,4,5,'abc']

if 5 in arr:
    print('{name} found {test}'.format(name = inputValue, test = 'help'))
else:
    print('oops')

###################################################################################################################

arr1 = ['1','2']
arr2 = ['1','2']

print(arr1[0] is arr2[0])
arr2 = list(arr1)

# Lambda - cant have more than 1 logical operation. Дозволяє робити код компактнішим

def somefunc(a,c):
    print('a')
    print('c')
    return a * c

# func = lambda a, c: print('b'); print('b'); a * c
func = lambda a, c: a * c

print(somefunc(1,2))

print(func(1,2))

