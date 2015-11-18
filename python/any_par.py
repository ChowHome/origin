#!/usr/bin/python


def add(*nums):
	sum = 0
	for num in nums:
		sum += num	
	print 'sum is %s' %sum



add(1,2,3,4)
