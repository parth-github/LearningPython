import os
import pickle
'''
Pickle in Python is primarily used in serializing and deserializing a Python object structure. 
It's the process of converting a Python object into a byte stream 
to store it in a file/database, maintain program state across sessions, or transport data over the network.
'''
#Create pickle and save data
dict = { 'Test1': 1, 'Test2': 2, 'Test3': 3 }
filename = "test_pkl.pkl"
if not os.path.isfile(filename):
   with open(filename,'wb') as file:
       pickle.dump(dict, file)
   file.close() 

# Opening the pickle file
infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close() 

# Test the data
print(new_dict)
print(new_dict == dict)
print(type(new_dict))

#Output
#  {'Test1': 1, 'Test2': 2, 'Test3': 3}
#  True
#  <class 'dict'>
