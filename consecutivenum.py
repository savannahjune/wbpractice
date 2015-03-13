def find_consecutive(list_num, target):
    current_value = 0
    l_p = 0
    r_p = 0

    while current_value != target and r_p < len(list_num):
        print list_num[l_p], list_num[r_p], current_value, target
        if target > current_value:
            current_value += list_num[r_p]
            r_p += 1
        else:
            current_value -= list_num[l_p]
            l_p += 1

    if current_value == target:
        return list_num[l_p:r_p]

    return False

num = [1, 3, 4, 5, 6, 9, 1, 2, 3, 4, 5]
print find_consecutive(num, 12)

def move_zeroes_end(num_list):
    if len(num_list) == 0:
        return num_list

    end_pos = len(num_list)-1
    while end_pos > 0 and num_list[end_pos] == 0:
        end_pos -= 1

    i = 0
    while i < len(num_list) and i <= end_pos:
        if num_list[i] == 0:
            num_list[i] = num_list[end_pos]
            num_list[end_pos] = 0
            while end_pos > 0 and num_list[end_pos] == 0:
                end_pos -= 1
        i += 1

    if num_list[end_pos] != 0:
        end_pos += 1
    return end_pos, num_list

print move_zeroes_end([1, 0, 9, 7, 5, 0, 2, 1])
print move_zeroes_end([1, 0, 9, 7, 5, 0, 0, 1])
print move_zeroes_end([])
print move_zeroes_end([0])
print move_zeroes_end([0, 0])
print move_zeroes_end([1, 2])

def anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    # sort, convert to str and strip
    string1 = ''.join(sorted(string1)).strip()
    string2 = ''.join(sorted(string2)).strip()
    return string1 == string2

