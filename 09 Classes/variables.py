#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    # class variable mutable
    x = [1,2,3,4,5]

    def __init__(self, **kwargs):
        # object variable; don't touch directly; access through getter/setter
        # encapsulated variables in object
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    def type(self, t = None):
        if t: self._type = t
        return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    print(a0)
    print(a1)
    # accessing object variable not a good idea
    a0._sound = 'Joe'
    print(a0._sound, a1._sound) # only changed in a0 sound variable

    # class variable only exists in the class
    # not encapsulated
    a0.x[2] = 88 # changing class variable through one object
    print(a1.x) # change effect can be seen in other objects

if __name__ == '__main__': main()
