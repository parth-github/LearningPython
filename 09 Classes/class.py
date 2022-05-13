#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    # variable
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'
    # self is the reference to the object created from this class
    # method
    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)

def main():
    donald = Duck()
    print(donald.sound)
    donald.quack()
    donald.move()

if __name__ == '__main__': main()
