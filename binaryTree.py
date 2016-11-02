
#import binarytree

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self):
		self.root = 0
	def initTree(self, data):
		nodes = [None for i in data]
		self.root = TreeNode(data[0])
		nodes[0] = self.root
		i = 1
		while i < len(data):
			parent_index = int((i+1) / 2) - 1
			parent_node = nodes[parent_index]
			child_node = TreeNode(data[i])
			if i % 2:
				parent_node.left = child_node
			else:
				parent_node.right = child_node
			nodes[i] = child_node
			i += 1
		return self.root



data = [1, 2, 3, 4, 5]
'''
my_tree = binarytree.convert(data)
binarytree.pprint(my_tree)
'''

tree = BinaryTree()
print tree.initTree(data)