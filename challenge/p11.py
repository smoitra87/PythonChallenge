#! /usr/bin/env python

import string
import urllib2 , bz2, re
import pdb
import Image, ImageDraw
import sys;

""" solution to problem 11 in pythonchallenge http://www.pythonchallenge.com/pc/return/5808.html

    The Solution should be to demix two sets of pixels
"""

def main() :
   im = Image.open('cave.jpg') # Open image file   
   im.show();
   im_save = im.copy();
   data = im.getdata();
   #print(type(data));
   pix = im.load();
   (x0,y0,x1,y1) = im.getbbox() ; 
   print x0,y0,x1,y1 ;
   newIm = Image.new('RGB',(x1/2,y1));
   newImPix = newIm.load();
   for i in range(x0,x1,2) :
      for j in range(y0,y1): 
         if j%2 == 0 : 
            newImPix[i/2,j] = pix[i+1,j];
         else : 
            newImPix[i/2,j] = pix[i,j] ;
#   newIm.show();
   
   (x0,y0,x1,y1) = map(int, sys.argv[1:5])
   im.crop((x0,y0,x1,y1)).show();
   for i in range(x0,x1) :       
      print " "
      for j in range(y0,y1) : 
         sys.stdout.write(str(pix[i,j])+" ");
 
if __name__ == '__main__' :
    main()

