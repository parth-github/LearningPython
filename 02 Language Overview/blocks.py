#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73
# blocks are indentation at the same level
# blocks don't define scope of a variable
# function, objects and moduled define scope of a variable
if x < y:
    z = 112
    # '{}'.format(var)
    # or
    # f' string {var}'
    print('x < y: x is {} and y is {}'.format(x, y)) # practice on format method of string
    print('using outside variable in inner block {} --> {}'.format(x,y))
    print('z is in the scope of inner block where it is defined : {}'.format(z)) # accessible inside block where z var is defined
print('z is still in the same scope even outside the block : {}'.format(z)) # still accessible outside block

print(x if x>y else y)