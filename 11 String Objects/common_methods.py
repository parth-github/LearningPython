# case

print('Hello, world!'.upper())
print('Hello, world!'.lower())
print('Hello, world!'.capitalize())
print('Hello, world!'.title())

'''
The difference here is that casefold is similar to lower but it's more aggressive, and it removes all case distinctions, 
even in unicode. 
So if I use like a German sharp S here, and we run this, you notice that comes out to a lowercase ss.
'''
print('Hello, world!'.casefold()) 

# string is immutable
s1 = 'hello world'
s2 = s1.upper()
print(id(s1), id(s2)) # objects are different

# string concatenation
print(s1 + s2)
s3 = 'this string' ' that string' # another way for concatenation
print(s3)
