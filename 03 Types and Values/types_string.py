
x = 'se"v"en'
print(x) # string with double quote

# strings are immutable; hence string functions always return new string object
y = 'eight'
print(y.capitalize()) 
print(y.upper())
print(y) # actual y string obj has not changed

print(y.upper().lower().capitalize().casefold()) # functions can be used in chain

# string format method
a,b = 8,9
z = 'seven {} {}'.format(a, b) 
print(z)

print('six {} {}'.format(7, 8)) # taking direct value in format() argument
print('six {1} {0}'.format(7, 8)) # swap 7, 8
print('six "{1}" "{0}"'.format(7, 8)) # specify double quote
print('six "{1:9}" "{0:9}"'.format(7, 8)) # blank space left of the digit
print('six "{1:<9}" "{0:>9}"'.format(7, 8)) # blank at right and left
print('six "{1:<09}" "{0:>09}"'.format(7, 8)) # zero filling

print(f'six {a} {b}') # passing var
print(f'six "{a:<09}" "{b:>09}"')
print(f'six "{11:<09}" "{12:>09}"') # passing value\

a = True
b = False
x = ( 'bear', 'bunny', 'tree', 'sky', 'rain' )
y = 'bear'
# Strings are immutable objects hence shows same id (address)
print(id(y))
print(id(x[0]))