#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('lines.txt', 'rt') # read text file
    outfile = open('lines-copy1.txt', 'wt') # write text file
    for line in infile:
        # print(line.rstrip(), file=outfile) # can be used rstrip()
        # or
        outfile.writelines(line)
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
