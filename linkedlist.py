class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

def prnt(node):
	next = node.next
	print node.data
	if (next is not None):
		print next

# Iterative
def reverse(node):
	last = None
	current = node

	while(current is not None):
		next = current.next
		current.next = last
		last = current
		current = next

	return last

# Recursive
def recurse(node, last):
	if node is None:
		return last
	next = node.next
	node.next = last
	return recurse(next, node)

n0 = Node(4, None)
n1 = Node(3, n0)
n2 = Node(2, n1)
n3 = Node(1, n2)

print(n3)
result = recurse(n3, None)
prnt(result)