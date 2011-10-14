#! /usr/bin/env python

import string
import urllib2
import pickle
import pdb

""" solution to problem 5 in pythonchallenge http://www.pythonchallenge.com/pc/def/peak.html

Looks like there is a combination of pickle and ascii art
"""

def main() :
    # write data file onto directory
    #open('peakhell.p','w').write(urllib2.openurl('http://www.pythonchallenge.com/pc/def/banner.p').read())
    # read directly from the internet
    obj = pickle.load(urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
    for line in obj : print "".join(ch*count for ch, count in line)
  
if __name__ == '__main__' :
    main()

