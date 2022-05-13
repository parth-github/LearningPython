import os
print(os.getcwd())

f = open('12 File I-O/lines.txt')
# 'r' read mode
# 'w' write mode; creates the file if not exists
# 'a' append mode
# 'r+' read/write mode
# 'r+t' text mode
# 'r+b' binary mode
for line in f:
    print(line.strip())

