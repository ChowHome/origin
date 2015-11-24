#!/usr/bin/python

try:
	f = file('./passwd')
except:
	print ('File not found!')
	exit()


lines = f.readlines()

for i in lines:
	words = i.split(':')
	if words[0] == 'root':
		print (i,)

