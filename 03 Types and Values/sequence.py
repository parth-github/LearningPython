#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5 ]
# list is mutable
x[2] = 43
for i in x:
    print('i is {}'.format(i))

# tuple is immutable
y = (1,2,3,4,5,6)
#y[3] = 8 # will show error

# Sequence with range() excluding the end number
# range  is immutable
z = range(5)
#z[2] = 33 # trying to change member gives error
for i in z:
    print(i)

# to get a mutable list from range
zz = list(range(5))
zz[2] = 33
print(zz)

# dict is searchable pair of key-value pairs
d = {'one': 1, 'two': 2}
for k,v in d.items():
    print(f'{k}: {v}')