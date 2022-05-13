#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    # list sub game[]
    print_list(game[2])

    # slicing game[1:5:2]
    # search: game.index('Paper')
    # mutable: game.append('Computer')
    # insert at the beginning game.insert(0, 'PC')
    # remove by value: game.remove('Scissors')
    # pop to remove from end or from the particular index of the list game.pop(3)
    # del game[1:3]
    # join: print(','.join(game))
    # len(game)

    # tuples are immutable
    # append() method will not work in tuple


def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
