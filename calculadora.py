#!/usr/bin/python3

import sys
import operator

operations = {'suma': operator.add, 'resta': operator.sub, 'multiplicar': operator.mul, 'dividir': operator.truediv}

if len(sys.argv) != 4:
    print('Usage error: <operation> <num1> <num2>')
    sys.exit()

try:
    op = operations[sys.argv[1]]
except KeyError:
    print('Invalid operation')
    sys.exit()

print(op(int(sys.argv[2]), int(sys.argv[3])))
