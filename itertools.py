#-*- coding:utf-8 -*-
##http://wklken.me/posts/2013/08/20/python-extra-itertools.html
##https://docs.python.org/2/library/itertools.html
from itertools import *

#itertools.imap(function, *iterables)
#创建一个迭代器，生成项function(i1, i2, ..., iN)，其中i1，i2...iN分别来自迭代器iter1，iter2 ... iterN，如果function为None，则返回(i1, i2, ..., iN)形式的元组，只要提供的一个迭代器不再生成值，迭代就会停止。

def imap_test():
	for i in imap(lambda x:2*x, xrange(5)):
		print i
	for i in imap(lambda x,y:(x, y, x*y), xrange(5), xrange(5,10)):
		print '%d * %d = %d' % i

#itertools.count(start=0, step=1)
def count_test():
	for i in zip(count(1),["a","b","c"]):
		print i
#result:(1,"a")/n (2,"b")/n (3,"c")

#itertools.circle(iterable)
#itertools.repeat(object[,times])

#itertools.chain(*iterables): 
chain('abc','def') 	#---> a b c d e f
#itertools.compress(data, selectors) 筛选
compress('abcde',[1,0,1,0,1]) #---> a c e
#itertools.dropwhile(predicate, iterable)
#函数predicate(item)为true，则丢弃iterable里的项.若为false，则生成iterable的项和后续项。
dropwhile(lambda x:x < 5, [1,4,6,4,1]) #---> 6 4 1


#lambda,filter
def prime_numbers():
	nums = range(2, 50) 
	listi = [2,3,5,7]
	#for i in range(2,8):
	for i in listi: 
		nums = filter(lambda x: x == i or x % i, nums)
	print nums