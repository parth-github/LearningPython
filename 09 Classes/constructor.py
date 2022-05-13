#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    # special class method __init__()
    # initializes object variables as constructor
    def __init__(self, type, name, sound):
        # object variables starting with _ for not accessing directly
        self._type = type
        self._name = name
        self._sound = sound

    '''
    Alternatively:

    def __init__(self, **kwargs):
        # object variables starting with _ for not accessing directly
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten' # for giving default value
        self._name = kwargs['name']
        self._sound = kwargs['sound']

    # initialzing
    # no extra spaces around the = sign in paraemters
    a0 = Animal(type='Kitten', name='fluffy', sound='rarr')
    '''

    # getters
    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    # initialzes object with various parameters
    a0 = Animal('kitten', 'fluffy', 'rwar')
    a1 = Animal('duck', 'donald', 'quack')
    print_animal(a0)
    print_animal(a1)
    print_animal(Animal('velociraptor', 'veronica', 'hello'))

if __name__ == '__main__': main()
