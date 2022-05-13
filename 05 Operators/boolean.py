#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'

if a and b:
    print('expression is true')
else:
    print('expression is false')

if y not in x:
    print(f'{y} not in x')
else:
    print(f'{y} in x')

if y is not x[0]:
    print(f'{y} is not x[0]')
else:
    print(f'{y} is x[0]')