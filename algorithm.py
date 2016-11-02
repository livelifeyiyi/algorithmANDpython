#-*- coding:utf-8 -*-
#二分搜索：对于array有序数组,查找数组中包含的value值，返回value值的index.(log(2)N)
class binarySearch(object):
	def loop(self, array, value):
		left = 0
		right = len(array) - 1
		
		while left <= right:
			mid = left + (right-left) / 2
			if array[mid] < value:
				left = mid + 1
			elif array[mid] > value:
				right = mid - 1
			else: return mid
	def iterate(self, array, value, left, right):
		mid = left + (right-left) / 2
		if array[mid] == value:
			return mid
		elif array[mid] < value:
			self.iterate(array, value, mid + 1, right)
		elif array[mid] > value:
			self.iterate(array, value, left, mid - 1)