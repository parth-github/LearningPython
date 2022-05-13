#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# call by value:
# python takes copy of the value of that variable
# value is passed rather than object
# integer are immutable
def main():
   x = 5
   print(f'x is {x} & id: {id(x)}')
   kitten(x)
   print(f'x is {x} & id: {id(x)}')


def kitten(a):
    # a = 3 optionally arg can be defined in the function scope
   print(f'a is {a} & id: {id(a)}')
   a += 1
   print(f'a is : {a} & id: {id(a)}')

if __name__ == '__main__': main()