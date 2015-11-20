#!/usr/bin/env /usr/local/python3/bin/python3
# -*- coding: utf-8 -*-


'a test file'

__author__ = 'woodenZhou'



import sys

def test():

	if len(sys.argv) == 1:
		print ('Hello!')

	elif len(sys.argv) == 2:
		print ('Hello,' + sys.argv[1])

	else:
		print ('Too many arguments!')




if __name__ == '__main__':
	test()

