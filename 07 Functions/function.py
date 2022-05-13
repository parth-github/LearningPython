#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x = kitten()
    print(x) # calling x kitten() function is executed which returns no value hence None is printed

def kitten():
    print('Meow.')

if __name__ == '__main__': main()
# special variable __name__ returns the value of current module
# if the module is not imported by another module and run directly then its name is __main__ otherwise the module name
# 