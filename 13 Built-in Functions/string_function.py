# __repr__(str) prints the formatted return statement
# __str__(str) prints the 

class bunny:
    def __init__(self, n) -> None:
        self._n = n
    def __repr__(self) -> str:
        return f'repr: the number of bunnies is {self._n} \U0001f596'
    def __str__(self) -> str:
        return f'str: the number of bunnies is {self._n}'
    
x = bunny(47)
print(x) # calls __str__
print(repr(x)) # calls __repr__ with emoji
print(ascii(x)) # calls __repr__ with unicode character
print(chr(128406)) # prints the unicode character
print(ord('\U0001f596')) # gives number of character