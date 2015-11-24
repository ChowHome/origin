#!/usr/bin/env /usr/local/python3/bin/python3
# -*- coding: utf-8 -*-


'a test file'

__author__ = 'woodenZhou'
import time
import threading
import sys


counter = 0
 
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
 
    def run(self):
        global counter
        time.sleep(1);
        counter += 1
        print ("I am %s, set counter:%s" % (self.name, counter))
 
if __name__ == "__main__":
    for i in range(0, 200):
        my_thread = MyThread()
        my_thread.start()
