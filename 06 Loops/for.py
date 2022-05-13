#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor', 'mouse' )

for pet in animals:
    if pet is 'bunny': continue # avoid bunny to be pet
    if pet is 'velociraptor': break # exit the loop seeing this wild animal
    print(pet)
else: # executed when loop exits normally
    print("That's all about the pets")


