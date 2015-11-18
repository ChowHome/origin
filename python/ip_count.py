#!/usr/bin/python
import sys


if len(sys.argv) == 1:
	print ('Miss arg1!')
	exit()


fname = sys.argv[1]

try:
	f = open(fname)
except:
	print (fname + " is not found!")	


dic = {}


for line in f:
	ip = line.split()[0]
	if ip in dic: 
		dic[ip] += 1
	else:
		dic[ip] = 1



print dic





