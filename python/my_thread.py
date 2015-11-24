#!/usr/bin/env /usr/local/python3/bin/python3
# -*- coding: utf-8 -*-


'a test file'

__author__ = 'woodenZhou'
import time
import threading
import sys





def main(num):
	print (num)
	threading.Thread(target = proce, name = 'My_proc', args = (num,)).start()



def proce(num):
	print (num)
	time.sleep(1)




if len(sys.argv) != 2:
	print ('Usage:%s number' % sys.argv[0])
	exit()


if __name__ == '__main__':
	main(sys.argv[1])

