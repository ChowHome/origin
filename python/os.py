#!/usr/bin/env /usr/local/python3/bin/python3
# -*- coding: utf-8 -*-


'a test file'

__author__ = 'woodenZhou'

import os 

arr = [ x for x in os.listdir('/etc/') if os.path.isdir('/etc/' + x) ]

for i in arr:
	print (i)

