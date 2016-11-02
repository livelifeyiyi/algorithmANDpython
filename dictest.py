#!/usr/bin/python
#-*- coding UTF-8 -*-
match = {'(':')','[':']','{':'}'}
test = '()[]'
for i in test:
	
	if i in match:
		print i