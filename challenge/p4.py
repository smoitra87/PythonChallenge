#! /usr/bin/env python

import string
import urllib2
import pdb

""" solution to problem 4 in pythonchallenge http://www.pythonchallenge.com/pc/def/ocr.html

The trick is to send requests to the server and get the data that it responds with it. 
"""

def main() :
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=46059'
    for iter in range(400) :
        text2 = urllib2.urlopen(url).read()
        text = text2[text2.find('next nothing'):]
	nothing = "".join(ch for ch in text if ch.isdigit())
	url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % nothing
	print text2
 

if __name__ == '__main__' :
    main()

