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
   im2 = im.copy();
   pix2 = im2.load(); 
   newIm = Image.new('RGB',(x1/2,y1/2));
   newImPix = newIm.load();
   for i in range(x0+1,x1+1,2) :
      for j in range(y0,y1,2): 
         newImPix[i/2,j/2] = pix[i,j];
   newIm.show();
   (x0,y0,x1,y1) = newIm.getbbox() ; 
   print x0,y0,x1,y1 ;
   for i in range(x0+1,x1+1,2) :
      for j in range(y0,y1,2): 
         newImPix[i,j] = (0,0,0);
   newIm.show();

 
if __name__ == '__main__' :
    main()

