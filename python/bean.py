#!/usr/bin/env /usr/local/python3/bin/python3
# -*- coding: utf-8 -*-


'a test file'

__author__ = 'woodenZhou'



class Student(object):
	def __init__(self):
		pass
#		self.__name = name
#		self.__sex = sex


	def get_name(self):
		return self.__name

	def get_sex(self):
		return self.__sex


	def set_name(self,name):
		self.__name = name
	
	def set_sex(self,sex):
		self.__sex = sex



class Animal(Student):
	pass


dog = Animal()
dog.set_name('papi')
dog.set_sex('man')


print ('%s' %dog.get_name())


print (type(dog))

