# def  getNumberOfPrimes(N):
#     number_of_primes = 0
#     for i in xrange(N):
#     	if i == 2:
#     		number_of_primes = number_of_primes + 1
#         else if i % 2 == 0:
#         	continue

#             number_of_primes = number_of_primes + 1
#     return number_of_primes

# print getNumberOfPrimes(100)

# def convert_convert(N):
# 	binary_of_number = list(bin(N))
# 	# print binary_of_number
# 	new_string_bin = []
# 	for letter in binary_of_number[2:]:
# 		# print letter
# 		if letter == '1':
# 			new_string_bin.append('0')
# 		elif letter == '0':
# 			new_string_bin.append('1')
# 	# print new_string_bin
# 	converted_string = ''.join(new_string_bin)

# 	new_bin_int = int(converted_string, 2)

# 	return new_bin_int

# print convert_convert(50)

# def stone_possibilities(N, a, b):

# 	a_mult = N - 1
# 	b_mult = 0

# 	counter = N

# 	list_of_possibilties = []

# 	while counter > 0:
# 		possibility = (a * a_mult) + (b * b_mult)
# 		if possibility not in list_of_possibilties:
# 			list_of_possibilties.append(possibility)
# 		a_mult = a_mult - 1
# 		b_mult = b_mult + 1
# 		counter = counter - 1

# 	return list_of_possibilties

# print stone_possibilities(4, 10, 100)

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
def stone_possibilities(N, a, b):

	a_mult = N - 1
	b_mult = 0

	counter = N

	list_of_possibilities = []

	while counter > 0:
		possibility = (a * a_mult) + (b * b_mult)
		if possibility not in list_of_possibilities:
			list_of_possibilities.append(possibility)
		a_mult = a_mult - 1
		b_mult = b_mult + 1
		counter = counter - 1
	# print list_of_possibilities
	sorted_list = sorted(list_of_possibilities)
	# print sorted_list

	return sorted_list


line_number = 0
list_of_nums = []
for line in sys.stdin:
    line = line.rstrip('\n')
    list_of_nums.append(int(line))  
    line_number = line_number + 1
# print list_of_nums
index = 1
final_out = []
for i in xrange(list_of_nums[0]):
	output =  str(stone_possibilities(list_of_nums[index], list_of_nums[index+1], list_of_nums[index+2])).strip('[]')
	output = output.replace(',', '')
	final_out.append(output)
	index = index + 3
for output in final_out:
    sys.stdout.write(output + "\n") 

