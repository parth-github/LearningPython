#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    #print_dict(animals)
    print(animals)
    # or initialization using dict() constructor
    d = dict(Buffy = 'meow', Zilla = 'grr', Angel = 'rawr')
    print(d)

    # accessing key, value
    for k, v in d.items():
        print(k,v)
        # get key for a value
        if v is 'grr': print(f'key of {v} is {k}')
    
    for k in d.keys():
        print('value at: ', d[k])
    
    for v in d.values():
        print(v)
    
    # dict values to list
    vals = d.values()
    print(vals, type(vals))
    vals_list = [v for v in d.values()]
    print(vals_list)

    # check key or values
    print('lion' in animals)
    print(animals['puppy'] if 'puppy' in animals else 'nope')

    # KeyError exception is that key is not exists

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')

if __name__ == '__main__': main()
