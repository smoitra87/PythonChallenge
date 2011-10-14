#! /usr/bin/env python

import string
import urllib2

""" solution to problem 2 in pythonchallenge http://www.pythonchallenge.com/pc/def/ocr.html

The solution is to extract the text within the HTML tags and thn find the rare characters. 
the word is equality
"""

def main() :
    response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
    try :
        page = response.read();
        junk  = page.partition('-->')[2].partition('<!--')[2].partition('-->')[0].strip()	
        junk_set = set(junk)
        for ch in junk_set :
            print ch, junk.count(ch)
        response.close()
    except Exception, e :
        print 'Exception occured and caught'
	print e
    finally :
        print 'Executing finally section'
        response.close()
    	

if __name__ == '__main__' :
    main()

