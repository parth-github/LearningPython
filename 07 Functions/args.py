#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    # used mainly to handle many args in a function call
    arg_list(1,2,3,4,5)
    kitten('meow', 'grrr', 'purr')
    
    # used to pass each elements as function args
    t = (11,22,33,44,55)
    kitten(*t)
    l = ['aa', 'bb', 'cc', 'dd', 'ee']
    kitten(*l)

    

def kitten(*args):
    if len(args):
        for s in args:
            print(s, end='~', flush=True)
    else: print('Meow.')

def arg_list(*l):
    for i in l:
        print(i, end='\t ', flush=True)
    print() # by default print a newline \n

if __name__ == '__main__': main()
