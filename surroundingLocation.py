#-*- coding: utf-8 -*-
#from collections import defaultdict
import math
class solution1(object):
	def calDistance(self, cen, loc):
		cenx, ceny = cen[0], cen[1]
		locx, locy = loc[0], loc[1]
		dis = math.sqrt(pow(cenx - locx, 2) + pow(ceny - locy, 2))
		return dis
	def solution1(self):
		num = 0
		for cen_key in cen.keys():
			r = cen[cen_key][2]
			for nxy_key in nxy.keys():
				if self.calDistance(cen[cen_key], nxy[nxy_key]) <= r:
					num += 1
			print num
			num = 0
class solution2(object):
	'''
	四叉树
	'''
	def __init__(self):
		#每个节点包含的点数限制，常量
		self.NODE_CAPACITY = 1
	def quardTreeNode(self, boundary, points, childNode):
		self.boundary = boundary	#该节点的范围，包含4个参数，区域的上下左右边界
		self.points = points	#该区域内节点的列表
		self.childNode = childNode	#包含4个参数，分别表示4个子区域
	def insert(self, nowNode, p):
		'''
		:param nowNode: quardTreeNode
		:param p: point
		:return: new treeNode
		将新的节点(x,y)插入时，若不在当前区域内，退出；
		否则将其加入该区域的节点列表points，若当前区域的节点列表已经满了。那么将该区域进行四分，同时将节点加入子区域中。
		'''
		if p not in nowNode.boundary:
			return nowNode
		if len(nowNode.points) < self.NODE_CAPACITY:
			nowNode.points.append(p)
		else:
			nowNode.devide()
			for i in nowNode.childNode:
				self.insert(i, p)
	def query(self, nowNode, range):
		'''
		四叉树的查询操作一般是求一个范围内的点，因此带入的参数也是一个区域range
		:param nowNode: quardTreeNode
		:param range:
		:return: pointsInRange,在范围内的点
		'''
		pointsInRange = []
		#该节点的区域与查询区域不相交
		if (not self.interSection(nowNode.boundary, range)):
			return None
		for p in nowNode.points:
			if p in range:
				pointsInRange.append(p)
		if nowNode.childNode:
			for childNode in nowNode.childNode:
				self.query(childNode, range)
		return pointsInRange


	def interSection(self, boundary, range):
		'''
		:param boundary: boundary of QuadtreeNode
		:param range:
		:return: bool, if the inputs have intersection
		'''


		

if __name__ == "__main__":
	#nxy = defaultdict(list)
	nxy = {}
	cen = {}
	(n, m) = (int(x) for x in raw_input().split(" "))
	i = j = 0
	while i < n:
		(x, y) = (int(x) for x in raw_input().split(" "))
		value = nxy.get(i, []) 
		nxy[i] = [x, y]
		i += 1
	while j < m:
		(a, b, r) = (int(x) for x in raw_input().split(" "))
		value = cen.get(j, []) 
		cen[j] = [a, b, r]
		j += 1
	