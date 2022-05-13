#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('berlin.jpg', 'rb') # rt will give UnicodeDecodeError: utf-8 codec can't decode 0xff in position 0: invalid start byte
    outfile = open('berlin-copy.jpg', 'wb')
    while True:
        buf = infile.read(10240) # 1KB buffer
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True) # print the progress bar
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
