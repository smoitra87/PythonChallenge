#! /usr/bin/env python

import string
import urllib2 , bz2, re
import pdb
import Image, ImageDraw

""" solution to problem 9 in pythonchallenge http://www.pythonchallenge.com/pc/return/good.html

    The trick is to draw a line using the coordinates in the source
"""

def main() :
     # Authenticate with website
     passw_mgr =  urllib2.HTTPPasswordMgrWithDefaultRealm()
     top_url = 'http://www.pythonchallenge.com/pc/return/'
     passw_mgr.add_password(None,top_url,'huge','file')
     handler = urllib2.HTTPBasicAuthHandler(passw_mgr)
     opener = urllib2.build_opener(handler)
     page = opener.open('http://www.pythonchallenge.com/pc/return/good.html').read()
     
     # Extract data from website
     first = page.partition('first:')[2].partition('second:')[0]
     second = page.partition('first:')[2].partition('second:')[2].partition('-->')[0]
     first =  map(int,first.replace('\n','').split(','))
     second =  map(int,second.replace('\n','').split(','))
     
     # Parse Data (Not required)
     first_line = [(first[i],first[i+1]) for i in range(0,len(first),2) ]
     second_line = [(second[i],second[i+1]) for i in range(0,len(second),2) ]

     # Draw image
     im_first = Image.new("L",(max(first[::2]),max(first[1::2])))
     draw_first = ImageDraw.Draw(im_first)
     draw_first.line(first,fill=255)
     draw_first.line(second_line,fill=255)
     im_first.show()
 
if __name__ == '__main__' :
    main()

