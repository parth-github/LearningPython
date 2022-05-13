#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# hexadecimal numbers starts with 0x
x = 0x0a
y = 0x02
z = x & y
v = ~x
# print in hex and binary
# hex format -> {var: filling_number number_of_places x}
# bin format -> {var: filling_number number_of_places b}
print(f'(hex) x is {x:06x}, y is {y:06x}, z is {z:06x}')
print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:08b}')
print(f'(bin) is {v:08b}, (dec) is {v}, hex is {v:06x}')