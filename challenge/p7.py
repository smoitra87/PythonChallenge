#! /usr/bin/env python

import string
import urllib2 , Image
import pdb

""" solution to problem 7 in pythonchallenge http://www.pythonchallenge.com/pc/def/oxygen.html

 The solution is to use the Image toolbox to examine the grey region and look for ascii code 
"""

def main() :
    open('oxygen.png','w').write(urllib2.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()) # save image file     
    im = Image.open('oxygen.png') # open image
    im2 = im.crop((1,50,629,51))
    im2.show()
    data = list(im2.getdata())	
    msg = "".join(chr(pix[1]) for pix in data[::7])
    print msg
    code = [105,110,116,101,103,114,105,116,121]
    print "".join(chr(ch) for ch in code)

  
if __name__ == '__main__' :
    main()

