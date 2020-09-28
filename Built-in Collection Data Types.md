Lists, strings, and tuples are ordered collections
Sets and dictionaries are unordered collections.


Method Name Use Explanation
append a_list.append(item) Adds a new item to the end of a list
insert a_list.insert(i,item) Inserts an item at the �th position in a list
pop a_list.pop() Removes and returns the last item in a list
pop a_list.pop(i) Removes and returns the �th item in a list
sort a_list.sort() Modifies a list to be sorted
reverse a_list.reverse() Modifies a list to be in reverse order
del del a_list[i] Deletes the item in the �th position
index a_list.index(item) Returns the index of the first occurrence of item
count a_list.count(item) Returns the number of occurrences of item
remove a_list.remove(item) Removes the first occurrence of item
Table 1.3: Methods Provided by Lists in Python


>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(5,10)
range(5, 10)
>>> list(range(5,10))
[5, 6, 7, 8, 9]
>>> list(range(5,10,2))
[5, 7, 9]
>>> list(range(10,1,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2]



