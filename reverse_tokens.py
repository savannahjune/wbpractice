string = "Code is so cool"

def reverse_tokens(string):
	tokens = string.split()
	reverse_list = []

	for item in tokens:
		reverse_list.insert(0, item)
	
	print (" ").join(reverse_list)


reverse_tokens("Code is so cool")

