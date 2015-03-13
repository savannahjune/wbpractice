def hill(v):
    # Write your code here
    # To print results to the standard output you can use print
    # Example print "Hello world!"
    sorted_v = sorted(v)
    max_diff = 0
    index = 0
    for number in v:
        diff = abs(number - sorted_v[index])
        if diff > max_diff:
            max_diff = diff
        index += 1
    print max_diff

hill([5, 4, 3, 2, 8])