def main():
   x = [5]
   print(f'before func call: x is {x} & id of x: {id(x)} & id of x[0] : {id(x[0])}')
   kitten(x)
   print(f'after func call: x is {x} & id: {id(x)} & id of x[0] : {id(x[0])}')


def kitten(a):
    # a = 3 optionally arg can be defined in the function scope
   print(f'before changing value: a is {a} & id: {id(a)} & id of a[0] : {id(a[0])}')
   a[0] += 1
   print(f'after changing value a is : {a} & id: {id(a)} & id of a[0] : {id(a[0])}')

if __name__ == '__main__': main()