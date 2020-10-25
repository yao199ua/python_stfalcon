test_tuple = ('apple','kiwi','banana')

print(test_tuple[0])

test_arr = ['apple','kiwi','banana']

print(test_arr[0])

test_arr[0] = 'cola'

print(test_arr[0])

#tuple with 1 element:

test_tuple2 = ('apple',)

print(type(test_tuple2))

test_tuple3 = test_tuple + test_tuple2
print(test_tuple3)
print(test_tuple3.count('apple'))

import sys

print('number of arguments: ')
#print(len)
print(sys.argv)
'''
a = int(sys.argv[1])
b = int(sys.argv[2])

print(a+b)
'''

import argparse

ar = argparse.ArgumentParser()
ap.add_argument('-n', '--name', required = False, help='description')

params, tmp = ap.parse_known_args()
print(tmp)
print(params)

#Fin.


