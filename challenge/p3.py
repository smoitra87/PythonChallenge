#! /usr/bin/env python

import string
import urllib2
import pdb

""" solution to problem 3 in pythonchallenge http://www.pythonchallenge.com/pc/def/ocr.html

The solution is to replace all capital letters with 1 and small by 0
Then do a string search for 1110111. 
"""

def main() :
    response = urllib2.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
    try :
        page = response.read();
        junk  = page.partition('<!--')[2].partition('-->')[0].strip()	
	#pdb.set_trace()
    except Exception, e :
        print 'Exception occured and caught'
	print e
	raise
    else : 
	print 'No Exception occured. Executing else section'
        #print 'junk is %s ' % junk
        trans = string.maketrans(string.ascii_lowercase+string.ascii_uppercase,
	'0'*len(string.ascii_lowercase)+'1'*len(string.ascii_uppercase))
	sense = junk.translate(trans)
	print 'The solution is : '
	pointer = -1
	while True :	
	    pointer = sense.find('011101110',pointer+1)	
	    #pdb.set_trace()
	    if pointer == -1 : break
	    else : print junk[pointer+4]
    finally :
        print 'Executing finally section'
        response.close()
    	

if __name__ == '__main__' :
    main()

