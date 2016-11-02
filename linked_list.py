#-*- coding: utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class LinkList(object):
	def __init__(self):
		self.head = 0
	def initlist(self, data):
		self.head = ListNode(data[0])
		p = self.head
		for i in data[1:]:
			node = ListNode(i)
			p.next = node
			p = p.next
		return self.head

class Solution(object):
	def getlength(self, head):
		p = head
		length = 0
		while p.next:
			length += 1
			p = p.next
		return length
	def reverseList(self, head):
		if not head or not head.next:
			return head
		pre = next = ListNode(None)
		pre = pre.next
		while head:
			next = head.next
			head.next = pre
			pre = head
			head = next
		return pre
	#删除倒数第k个节点
	def delkthNode(self, head, k):
		p1 = p2 = head
		for i in range(0, k):
			p2 = p2.next
		while p2.next:
			p1 = p1.next
			p2 = p2.next
		p1.next = p1.next.next
		return head
	#中间节点
	def middleNode(self, head):
		slow = fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		return slow

	def hasCycle(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		slow = fast = head
		while (fast and fast.next):
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return True
		return False

	def detectCycle(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		slow = fast = head
		while True:
			if fast == None or fast.next == None: return None
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				break
		fast = head
		while (fast != slow):
			slow = slow.next
			fast = fast.next
		return fast

data = [1, 2, 3, 4, 7]
l = LinkList()
head = l.initlist(data)
S = Solution()
print S.middleNode(head)