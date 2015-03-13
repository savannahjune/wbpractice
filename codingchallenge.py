def check_anagrams(first_words, second_words):
    # Write your code here
    # To print results to the standard output you can use print
    # Example print "Hello world!"
    index = 0
    for item in first_words:
        sorted_item = sorted(item)
        sorted_second_item = sorted(second_words[index])
        if sorted_item == sorted_second_item:
            print 1
        else: 
            print 0
        index+=1
        
check_anagrams(["cinema","host","aba","train"], ["iceman","shot","bab","rain"])

def anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    # sort, convert to str and strip
    string1 = ''.join(sorted(string1)).strip()
    string2 = ''.join(sorted(string2)).strip()
    return string1 == string2


def check_braces(expressions):
    # Write your code here
    # To print results to the standard output you can use print
    # Example print "Hello world!"
    dict={'(':0, '[':0, '{':0}
    for braces in expressions:
        for brace in braces:
            if brace == '(':
                dict['('] += 1
            if brace == '[':
                dict['['] += 1
            if brace == '{':
                dict['{'] += 1
            if brace == ')':
                dict['('] -= 1
            if brace == ']':
                dict['['] -= 1
            if brace == '}':
                dict['{'] -= 1
    for key, value in dict.iteritems():
        if value != 0:
            print 0
            return
    print 1