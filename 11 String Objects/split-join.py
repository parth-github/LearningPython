#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# string with newline multispace
s = '''This is a long       string with     
a bunch of     words in it.'''

print(s) # print as it is with multi line
print(s.split()) # by default split by all whiteline characters
print(s.split(' ')) # split with space 
print(s.split('i'))

splitted_list = s.split()
print(f'split by default {splitted_list}')
joined_str = '+'.join(splitted_list)
print(joined_str)

