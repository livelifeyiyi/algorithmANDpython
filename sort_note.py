#-*- coding:utf-8 -*-
import math
######################
#插入排序
######################
def insertSort(list):
	for j in range(1, len(list)):
		key = list[j]
		i = j-1
		while i >= 0 and list[i] > key:
			list[i + 1] = list[i]
			i -= 1
		list[i + 1] = key
	return list
######################
#冒泡排序
######################
'''
冒泡排序算法的流程如下：
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
'''
def bubbleSort(list):
	'''for i in range(0, len(list)-1):
		for j in range(i + 1, len(list)):
			if list[i] > list[j]:
				list[i],list[j] = list[j],list[i]'''
	for i in range(1, len(list)):
		for j in range(0, len(list)-i):
			if list[j] > list[j+1]:
				list[j], list[j+1] = list[j+1], list[j]
	return list
def better_bubbleSort(list):
	n = len(list)
	flag = n
	while flag > 0 :
		k = flag
		flag = 0
		for j in range(1, k):
			if list[j-1] > list[j]:
				list[j-1], list[j] = list[j], list[j-1]
				flag = j + 1
	return list
######################
#归并排序
######################
'''
将待排序序列A[0,1...n-1]看成是n个长度为1的有序序列，将相邻的有序列成对归并，得到n/2个长为2的有序表；
再将这些有序序列再次归并，得到n/4个长为4的有序序列，反复进行，得到长度为n的有序序列。
'''
def mergeSort(list):

	def merge(A, first, mid, last):
		n1 = mid - first +1
		n2 = last - mid
		#left, right = [], []
		left = A[first:mid+1]
		right = A[mid+1:last+1]

		res = []
		i = j = 0
		#for k in range(0, n1 + n2):
		while i < n1 and j < n2:
			if left[i] < right[j]:
				res.append(left[i])
				i += 1
			else:
				res.append(right[j])
				j += 1
		while i < n1:
			res.append(left[i])
			i += 1
		while j < n2:
			res.append(right[j])
			j += 1
		k = 0
		for i in range(first, last+1):
			A[i] = res[k]
			k += 1

	'''
	def sort(A, first, last):
		if first < last:
			mid = int(math.floor((last+first)/2))
			sort(A, first, mid)
			sort(A, mid+1, last)
			merge(A, first, mid, last)
		return A
	'''
	def sort(A, gap, length):
		i = 0
		while i + 2*gap - 1 < length:
			merge(A, i, i+gap-1, i+2*gap-1)
			i += 2* gap
		if i + gap -1 < length:
			merge(A, i, i+gap-1, length-1)
		return A
	gap = 1
	while gap < len(list):
		A = sort(list, gap, len(list))
		print "gap="+ str(gap) +str(A)+"\n"
		gap = 2 * gap
	return A

######################
#堆排序
######################
def parent(i):
	return (i-1) / 2
def leftChild(i):
	return 2*i + 1
def rightChild(i):
	return 2*i + 2

#最大堆，小的向下移
def MaxHeapfy(A, i, n):
	#n = len(A)
	l = leftChild(i)
	r = rightChild(i)
	if l < n and A[l] > A[i]:
		largest = l
	else: largest = i
	if r < n and A[r] > A[largest]:
		largest = r
	if largest != i:
		A[i], A[largest] = A[largest], A[i]
		MaxHeapfy(A, largest, n)
def builfMaxHeap(A, n):
	#n = len(A)
	i = (n-1)/2
	while i >= 0:
		MaxHeapfy(A, i, n)
		i -= 1
def HeapSort(A):
	n = len(A)
	builfMaxHeap(A, n)
	i = n-1
	while i >= 1:
		A[0], A[i] = A[i], A[0]
		n -= 1
		MaxHeapfy(A, 0, n)
		i -= 1
	return A

print HeapSort([5,2,4,6,1,3,7])




######################
#快速排序
#最坏O(n), 期望O(nlgn)
######################
def quickSort(list, left, right):
	if left < right:
		mid = partition2(list, left, right)
		quickSort(list, left, mid-1)
		quickSort(list, mid+1, right)
	return list
def partition(list, left, right):
	#n = right - left + 1
	i = left-1
	#以最右数作为主元,比主元大的向右移，小的向左移.i指向小的，j指向大的
	key = list[right]
	for j in range(left, right):
		if list[j] <= key:
			i += 1
			list[i], list[j] = list[j], list[i]
	list[i+1], list[right] = key, list[i+1]
	return i+1
'''
1. i =L; j = R; 将基准数挖出形成第一个坑a[i]。
2．j--由后向前找比它小的数，找到后挖出此数填前一个坑a[i]中。
3．i++由前向后找比它大的数，找到后也挖出此数填到前一个坑a[j]中。
4．再重复执行2，3二步，直到i==j，将基准数填入a[i]中。
'''
def partition2(list, left, right):
	key = list[left]
	i, j = left, right
	while i<j:
		while i < j and list[j] >= key:
			j -= 1
		if i < j:
			list[i] = list[j]
			i += 1
		while i < j and list[i] < key:
			i += 1
		if i < j:
			list[j] = list[i]
			j -= 1
	list[i] = key
	return i

#list = [2,8,7,1,3,5,6,4]
#print quickSort(list, 0, len(list)-1)


#print mergeSort([5,2,4,6,1,3,7])
