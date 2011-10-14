#! /usr/bin/env python

import string
import urllib2 , zipfile
import re
import pdb

""" solution to problem 6 in pythonchallenge http://www.pythonchallenge.com/pc/def/channel.html

The trick is that there is a channel.zip file. 
"""

def main() :
    open('channel.zip','w').write(urllib2.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip').read()) 	   
    zipObj = zipfile.ZipFile('channel.zip','r')
    findnothing  = re.compile('nothing is (\d+)').findall
    curr = '90052' 
    zipInfoDict = zipObj.NameToInfo
    msg = ''
    while True : 
        try : 
            text = zipObj.read(curr+'.txt')
	    #print text	
	    msg = msg+(zipInfoDict[curr+'.txt'].comment)	
            curr = findnothing(text)[-1]
        except Exception, e : 
            print 'Exception occured and caught'
	    print e
            break	
    print 'The message is of length %d '  % len(msg)
    print msg
  
if __name__ == '__main__' :
    main()

