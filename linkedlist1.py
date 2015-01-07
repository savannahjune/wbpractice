class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def append_node(self, node):
		if self.tail is not None:
			self.tail.next = node

		self.tail = node

		if self.head is None:
			self.head = node

	def __repr__(self):

		node = self.head

		rep = ''
		while node is not None:
			rep += str(node.value)

			if node.next is not None:
				rep += ' -> '

			node = node.next

		return rep

class Node:

	def __init__(self, value):
		self.value = value
		self.next = None

	def set_next(self, next):
		self.next = next

list = LinkedList()

a_node = Node(5)
b_node = Node(7)
c_node = Node(9)

list.append_node(a_node)
list.append_node(b_node)
list.append_node(c_node)

print list


