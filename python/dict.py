#!/usr/bin/env /usr/local/python3/bin/python3
# -*- coding: utf-8 -*-

dic = {'name':'snake','sex':'man'}


for key in dic:
        print (key)

for val in dic.values():
	print (val)



for key,val in dic.items():
	print ('%-8s->%s' %(key,val))

