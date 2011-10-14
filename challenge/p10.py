#! /usr/bin/env python

import string
import urllib2 , bz2, re
import pdb
import Image, ImageDraw

""" solution to problem 10 in pythonchallenge http://www.pythonchallenge.com/pc/return/bull.html

    The trick is to generate something known as Morris numbers
"""

def morris(last) :
    if not last : return None
    curr = last[0]
    count = 0
    sol = ''
    for i in range(len(last)) : 
        if last[i] == curr : 
           count += 1
        else :
           sol += str(count)+str(curr) # add string to solution
           curr = last[i]
           count = 1
    sol += str(count)+str(curr) # to flush the last string
    return sol

def genMorris(N) :
     
    for i in range(N) : 
        if  i == 0 : 
            last = '1'
            yield '1' 
        else : 
             last = morris(last)
             yield last

def main() :
    N = 31 # number of morris numbers needed
    seq = [last for last in genMorris(N)] # using generators :)
    print len(seq[30])
    #print seq
    #pdb.set_trace()
 
if __name__ == '__main__' :
    main()

