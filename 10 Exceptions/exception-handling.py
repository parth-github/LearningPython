#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
import sys


import sys

def main():
    # handling errors
    #ValueError
    try: # catch the error
        x = int('foo')
        y = 5/0
    except ValueError:
        print('got a value error')
        # handle the error
    except ZeroDivisionError  as e:
        print("Don't divide by zero: {e}")
    except:
        print('Unkonwn error: {sys.exec_info()}')
        print(f'range error: {e}')
    else: # succeeds if having no errors
        print('good job')
    finally:
        print('Close the program')

if __name__ == '__main__': main()
