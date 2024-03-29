#! /usr/bin/env python

import string
import urllib2 , bz2
import pdb

""" solution to problem 8 in pythonchallenge http://www.pythonchallenge.com/pc/def/integrity.html

 The solution is to use the bz2 module to decode the username and the password
in the source page 
"""

def main() :
    un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    print bz2.decompress(un)
    print bz2.decompress(pw) 
  
if __name__ == '__main__' :
    main()

