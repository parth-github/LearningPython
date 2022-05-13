#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    seq = range(11)
    print_list(seq)
    
    # create list from list
    sq_list = [x**2 for x in seq] # for loop 
    sq_list_squared = [x**2 for x in seq if x %2 != 0] # for loop with filter
    
    # create tuple from list
    sq_tuple = [(x, x**2) for x in seq]
    import math
    sqrt_tuple = [(x, math.sqrt(x)) for x in seq]

    # create dict from list
    sq_dict = {x: x**2 for x in seq}

    # create set from list/string
    example_str = 'The quick brown fox jumps over the lazy dog'
    pangram_set = {x for x in example_str if x is not ' '}
    print(pangram_set, len(pangram_set))

def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()
