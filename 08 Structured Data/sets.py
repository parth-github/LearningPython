#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)
    # sorted
    print(sorted(a))
    print(sorted(b))
    # check the members in set
    print(a | b) # union
    print(a & b) # intersection
    print(a - b) # minus
    print(a ^ b) # xor

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
