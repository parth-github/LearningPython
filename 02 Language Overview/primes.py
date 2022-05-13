#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n):
         if n % x == 0: # comment
            return False
    else: return True
primes = []
def list_primes():
    for n in range(100):
        if isprime(n): 
            primes.append(n)
            print(n, end='_', flush=True)
    return primes
print(list_primes()) # call by reference
print(primes)
n = 6
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} not prime')


