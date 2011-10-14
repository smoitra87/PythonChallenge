#! /usr/bin/env python

import string

""" solution to problem 1 in pythonchallenge http://www.pythonchallenge.com/pc/def/map.html

The solution is to Shift every letter by 2 characters
"""

def main() :
    print 'Call to main executed'
    ascii = 'abcdefghijklmnopqrstuvwxyz'
    ascii2 = ascii[2:26]+ascii[0:2]
    trans_table = string.maketrans(ascii,ascii2)
    s = """ g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. """
    t = """pc/def/map.html"""
    print(s.translate(trans_table))
    print(t.translate(trans_table))

if __name__ == '__main__' :
    main()

