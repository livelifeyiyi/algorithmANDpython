# -*- coding: utf-8 -*-
#给定文本text和模式pattern,判断pattern是否在text出现,并返回出现的位置偏移(index)
##朴素算法O((n-m+1)m)
def naiveStringMatcher(text, pattern):
	n, m = len(text), len(pattern)
	for s in range(n - m):
		if text[s:s+m] == pattern[0:m]:
			return s

#print naiveStringMatcher('abccdef','ccd')

##Rabin-Karp算法O((n-m+1)m)
def RPmatcher(text, pattern, d, q):
	'''
	d:进制
	q:需取模的值，选取合适的值
	'''
	n, m = len(text), len(pattern)
	h = pow(d, m-1) % q

	p = 0
	t = [0] * (n - m)		#记录每个text取m个数的段 对应十进制的值
	#preprocessing,O(m)
	for i in range(m):
		p = (d*p + int(pattern[i])) % q	#d=10时，计算pattern对应十进制的值 并% q
		t[0] = (d*t[0] + int(text[i])) % q	#计算text[0:m]对应十进制的值 并% q，赋值给t[0]
	print p, t[0]
	for s in range(n-m):
		print t[s]
		if p == t[s]:
			if pattern == text[s:s+m]:	#监测s对应的字符串是真得匹配还是伪命中点
				return s
		if s < n-m:
			t[s+1] = (d*(t[s] - int(text[s]) * h) +  int(text[s+m])) % q 	#减去高位数,右移一位*d,加低位数

#print RPmatcher('2359023141526','31415',10, 13)
def computePrefixFunction(pattern):
	'''
	func[q] = k, pattern k 是pattern q的后缀
	p5:ababa,p3:aba, func[5]=3
	'''
	m = len(pattern)
	func = [0] * m
	length = 0
	for q in range(1, m):
		while length > 0 and pattern[length] != pattern[q]:
			length = func[length-1]
		if pattern[length] == pattern[q]:
			length += 1
		func[q] = length
	return func

def KMPmatcher(text, pattern):
	n, m = len(text), len(pattern)
	func = computePrefixFunction(pattern)
	print func
	q = 0
	for i in range(1, n):
		while q > 0 and pattern[q] != text[i]:
			q = func[q-1]
		if pattern[q] == text[i]:
			q += 1
		if q == m:
			print i-m+1
			q = func[q-1]  #look for the nexr match

print KMPmatcher('bacbababaabc','abab')