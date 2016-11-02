#-*- coding:utf-8 -*-
#插入排序
def insertSort(list):
	for j in range(1, len(list)):
		key = list[j]
		i = j-1
		while i >= 0 and list[i] > key:
			list[i + 1] = list[i]
			i -= 1
		list[i + 1] = key
	return list
#冒泡排序
def bubbleSort(list):
	for i in range(0, len(list)-1):
		for j in  range(i + 1, len(list)):
			if list[i] > list[j]:
				list[i],list[j] = list[j],list[i]
	return list			
#归并排序

#堆排序

#快速排序


print bubbleSort([5,2,4,6,1,3])
