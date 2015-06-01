#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import time
import binascii
from libmich.formats import *

TESTCALL_PORT = 28670
#len = 19
#lai = 42
#hexstr = "051a00f110"
#hexstr += "%02x%02x%02xfc" % (lai>>8, lai&255, (4*len+1))
#hexstr += ''.join('%02x666666' % (4*i) for i in range(len))
hexstr = "\x03\x3D"
print "layer3 message to be sent:", hexstr
#l3msg = binascii.hexlify(hexstr)
l3msg = hexstr;

print "libmich interprets this as: ", repr(L3Mobile.parse_L3(l3msg))

tcsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tcsock.settimeout(1)
try:
	tcsock.sendto(l3msg, ('127.0.0.1', TESTCALL_PORT))
	reply = tcsock.recv(1024)
	print "reply : " , reply
	print "reply received: ", repr(L3Mobile.parse_L3(reply))
except socket.timeout:
	print "no reply received. potential crash?"