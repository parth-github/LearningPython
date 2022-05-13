#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.'.upper())
print('Hello, World.'.swapcase())
print('Hello, World.{}'.format(42 * 7))

print('''
Hello, 
World.
{}'''.format(42 * 7))

s = 'Hello, World.{}'
print(s.format(42*7))

class MyString(str):
    def __str__(self) -> str:
        #return super().__str__()
        # print reverse
        return self[::-1]

a = MyString('Hello, World.')
print(a)