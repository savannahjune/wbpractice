# class BinaryTree(object):
# 	def __init__(self,root):

class BinaryTreeNode(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
		self.parent = None

	def set_parent(parent):
		self.parent = parent

	def get_left(self):
		return self.left

	def set_left(self, node):
		if self.get_left(self) == None:
			# if there is nothing to the left place the node there
			self.left = node
			node.parent = self
			return
		else:
			# if there is something to the left, move your pointer to that node on the left 
			# and recursively check if there is anything to the left of that
			return (self.left).set_left(node)

	def get_right(self):
		return self.right

	def set_right(self, node):
		#self is parent!
		if self.get_right(self) == None:
			self.right = node
			node.parent = self
			return
		else:
			return (self.right).set_right(node)

	def get_value(self):
		return self.value

	def set_value(self, number):
		if self.get_value(self) == None:
			self.value = number
    
def breadth_first_traversal(root):


def test_tree():
	root = BinaryTreeNode(1)
	left = BinaryTreeNode(2)
	right = BinaryTreeNode(3)
	root.set_left(left)
	root.set_right(right)





