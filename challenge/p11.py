#! /usr/bin/env python

import string
import urllib2 , bz2, re
import pdb
import Image, ImageDraw

""" solution to problem 11 in pythonchallenge http://www.pythonchallenge.com/pc/return/5808.html

    The Solution should be to demix two sets of pixels
"""

def main() :
   im = Image.open('cave.jpg') # Open image file   
   # im.show();
   im_save = im.copy();
   data = im.getdata();
   #print(type(data));
   pix = im.load();
   (x0,y0,x1,y1) = im.getbbox() ; 
   print x0,y0,x1,y1 ;
   newIm = Image.new('RGB',(x1/2,y1/2));
   newImPix = newIm.load();
   for i in range(x0,x1,2) :
      for j in range(y0,y1,2): 
         if j%2 == 0 : 
            newImPix[i/2,j/2] = pix[i+1,j];
         else : 
            newImPix[i/2,j/2] = pix[i,j] ;
   newIm.show();
   pdb.set_trace();
 
if __name__ == '__main__' :
    main()

