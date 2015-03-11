class Node(object):
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
	next = None
	current = node

	while(current is not None):
		# keep track of the current.next for next batch
		next = current.next
		# reversing pointer on your current node
		current.next = last
		# creating conditions for next step through for next go round
		# last will be the node you are currently manipulating
		# and current will be the next node that you kept track of in line 19
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