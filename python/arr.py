#!/usr/bin/python



word = raw_input('User:')
arr = []


while word <> 'exit':

	arr.append(word)

	word = raw_input('User:')





while arr:
	print arr.pop(0)


