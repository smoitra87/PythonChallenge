#! /usr/bin/env python

import string
import urllib2 , bz2, re
import pdb
import Image, ImageDraw
import sys;

""" solution to problem 12 in pythonchallenge http://www.pythonchallenge.com/pc/return/5808.html

    
"""

def main() :
  with open('evil2.gfx','rb') as fin :
     temp = fin.readlines();
     for ii, line in enumerate(temp) : 
        print ii , line ; 
    
 
if __name__ == '__main__' :
    main()

