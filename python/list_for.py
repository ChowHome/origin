#!/usr/bin/env /usr/local/python3/bin/python3
# -*- coding: utf-8 -*-

import os

arr = [ i for i in range(1,11) if i %2 == 0]
print (arr)


arr = [ i for i in 'snake' ]
print (arr)


#files = [ f afor f in os.listdir('/etc/') ] 
#print (files)


arr = [ i.upper() for i in 'snake' ] 
print (arr)


