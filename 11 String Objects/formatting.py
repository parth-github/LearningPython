
x = 42

print('the number is {}'.format(x))

y = 73

print('the number is {} {}'.format(x, y))
print('the number is {b} {a}'.format(a=x, b=y))
print('the number is {1} {0} {1}'.format(x, y))

print('the number is {0:<5} {1:>5}'.format(x, y))
print('the number is {0:<05} {1:>05}'.format(x, y))
print('the number is {0:<05} {1:+05}'.format(x, y))

z = 42 * 747 * 1000
print(z)
print('The number is {:,}'.format(z).replace(',', '.'))
print('The number is {:.3f}'.format(z))
print('The number is {:b}'.format(z))
print('The number is {:x}'.format(z))
print('The number is {:o}'.format(z))

print(f'the number {z}') # Python 3.6+ 
# f is replacement of format()