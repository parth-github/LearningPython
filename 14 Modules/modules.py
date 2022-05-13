#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from random import random
import sys, os
import random
import datetime

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    print(type(v), v)
    
    print(sys.version)
    print(sys.platform)
    print(os.name) # posix : unix, nt : windows
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(25).hex()) # 25 bytes hex number

    x = random.randint(1,1000)
    print(x)

    y = list(range(25))
    random.shuffle(y)
    print(y)

    now = datetime.datetime.now()
    print(now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second)

if __name__ == '__main__': main()
