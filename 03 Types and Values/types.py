#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 7
print('x is {}'.format(x))
print(type(x)) # shows type class int or int object

y = (1, 'four', 'two', 3.0, [5,6,7], )
z = (1, 'two', 3.0, [5,6,7]) # y, z both are having same tuple value
print(id(y), id(z)) # shows y and z both are different objects though their values are same
print(id(y[0]), id(z[0])) # shows same object location since both are pointing to int object 1
print(id(y[2]), id(z[1])) # shows same object location since both are pointing to same str object 'two'
print(id(y[3]), id(z[2])) # shows same object location since both are pointing to same float object 'two'
print(id(y[4]), id(z[3])) # list are different like tuple, they are sequence type

#############
if y[0] == z[0]: print('Yes') # always true

if type(y) is type(z): # checking both type are same
    print('yes: both type are same') 
else: 
    print('No')
# or
if y is z: # checking both object are same
    print('yes: both type are same') 
else: 
    print('No: obj y: {}, obj z:  {} are not same'.format(y,z))
##############
if isinstance(y, tuple): # if type(y) == 'tuple' will throw error
    print(f'y is tuple')

if not isinstance(y, list):
    print(f'y is not list')

# float value calculation
# precision vs accuracy
# float values follows precision
f = .1 + .2 + .3 - .6
print(f) # prints precision value 1.1102230246251565e-16
# to overcome this in money use decimal
# args are in string otherwise function takes precision value of float and return double precision
import decimal
f1 = decimal.Decimal('.1')
f2 = decimal.Decimal('.2')
f3 = decimal.Decimal('.3')
f4 = decimal.Decimal('.6')
ff = f1 + f2 + f3 - f4
print(ff)






