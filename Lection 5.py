# COMMAND LINE ARGUMENTS

# python -h in console = all available options and arguments
# -c
# -d
# -E


# python test.py arg1 arg2 arg3

import sys #дозволяє працювати з системними значеннями: environment variables etc.
'''
print('Number of arguments: ')
print(len(sys.argv))
print('Argument List: ' +str(sys.argv)) # Number of arguments: 1

print(sys.argv)
a = int(sys.argv[1])
b = int(sys.argv[2])

print(a_+b)  
IndexError: list index out of range ???????????????
'''


import argparse #розширює можливості для передачі параметрів

ar = argparse.ArgumentParser()
ap.add_argument('-n', '--name', required=False, help='some description')
# -n це зазвичай короткий параметр (?) --name - це коротка назва параметру. required означає чи параметр обов'язковий. 
# При True - все буде ламатись при парсингу. help = це просто підказка з якиомось описом.

'''
params, tmp = ap.parse_known_args()
print(tmp)
print(params.m)
# якщо функція повертає більше ніж 1 значення (????)
# якщо ми передамо при виклику якісь додаткові параметри, ... ???
'''