print('Hello world')
a = 2
b = 3
c = a+b

createdAt = '02.20.2020'

def sum(a,b):
    c = a+b
    print(c)
sum(5,3)

def getsummary():
    return 'Describe some summary information'
print(getsummary)

def example_method(self, param1, param2):
    '''
     Class methods are similar to regular functions.

    Note. Do not include the 'self' paramenter in the ''Args'' section.

    Args:
    param1: 1st parameter.
    param2: 2nd parameter.

    Returns: True if successful, False otherwise.
    '''
    return True

"""
Method apply a variable and b variable

Args:
    a: 1st par.
    b: 2nd par.

returns:
    int result of apply
"""

def summary(a,b):
    return a+b

result = sum(5,4)
print(sum)

someText =  'some very long text should be there \nwith a few extra lines\nDog, Cat, Parrot also was there.'
print(someText)

# \n = new line on output
# \n + \ = new line in the code as well

someText2 =  'some very long text should be there \n' +\
             'with a few extra lines\n' +\
             'Dog, Cat, Parrot also was there.'
print(someText2)

#Multiple statements per one line:

print('Multiple statements'); print('per one line')

# Indentation (відступи)

name = input('Enter name here:')

print('Hola')
if name == 'Bill':
    print(name)
else: 
    print('World')
print('Fin.')

name2 = input('Enter some name')

greeting = 'Hey, here is your special keyword list: ' + name2
print(greeting)

# List of special commands:

import keyword
print(keyword.kwlist)

#Booleans:

result = (1 == 1)

print(result)
if result:
    print('Noice')

result = (1 == 1 or 2 == 1)

print(result)
if result:
    print('Noice')

result = (1 == 1 and 2 == 1)

print(result)
if result:
    print('Noice')

if not a == b:
    print('print')

if a != b:
    print('print')

# None - empty function

def test_func():
    result = 1+1
    print(result)

tmp = test_func()
print(tmp) # < result is None

'''
^^^
x = 5
del x
#This would work in Python 2.x
print(x)
'''

None == 0
#False

None == []
#False

None == False
#False

x = None
y = None
x == y
#True

# in theory we can redefine None... but it might cause problems later. Same applies to other special keywords.
''' def None():
    return 2
print(None)
'''

#тернарний оператор:
a = 'abc' if True else 'cde'
print(a)

a = 'abc' if False else 'cde'
print(a)

# This is the same as above: ^^^
if True:
    print('abc')
else:
    print('cde')

#не більше 1 логічної операції в тернарний оператор:
'''
a = (a = 1+5; b = a*8; 'abc' + b) if  False else 'cde'
print(a)
'''
if True:
    a = 1+5
    b = a *8
    print(b)
else:
    print('cde')

# Switch (needs to be imported from a library)
a = 2

if a == 2:
    a = 1 + 5
    b = a * 8
    print(b)
elif a == 3:
    print(4)
else: 
    print('cde')


''' in other languages:
a = 2
switch(a) {
    case 2:
        a = 1+5
        b = a*8
        print(b)
        break;
    case 3:
        print(4)
    default:
        print('cde')
}
'''
a = 1 == 1
b = 1 == 2
print(a and b) # < will return False because both conditions have to be met.

a = 1 == 1
b = 2 == 2
print(a or b) # < returns True as only at least 1 conditions has to be met.

import math
print(math.pi)
# Math is the name of a library used for... math stuff
import math as myAlias 
myAlias.cos(myAlias.pi)
#AS allows to call something with another name if it has to be used for different purposes.
math = 'math test'
import math as math2
print(math)
print(math2.pi)

import math as math3
print(math3.cos(math2.pi)) # result = -1.0

#Assert: allows to check certain stetements or values whether they are true or not
#Often used in Unti Testing
'''
a = 4
assert a > 5, 'The value is too small'
AssertiomError: The value of a is too small
if a <= 5:
raise AssertionError('The value of a is too small')
'''
age = int(input('How old are you?'))
assert age > 18, 'You are too young'

age2 = int(input('How old are you?'))
assert age2 > 18, 'Convertation exception'
print('You can drive, yay!')

if age < 18:
    print('you cannot  drive a car')
    raise AssertionError('some text')
print('you can drive.')