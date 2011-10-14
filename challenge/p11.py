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

   # fn for subtracting tuples
   subt = lambda x,y : (x[0]-y[0],x[1]-y[1],x[2]-y[2]) 
   for i in range(x0,x1,2) :
      for j in range(y0,y1,2): 
         if j%2 == 0 : 
            pix2[i+1,j] = subt(pix2[i+1,j],pix[i,j]);
            #pdb.set_trace();
         else : 
            pix2[i,j] = subt(pix2[i,j],pix[i+1,j]);
   im.show();
   im2.show();
   pdb.set_trace();
 
if __name__ == '__main__' :
    main()

