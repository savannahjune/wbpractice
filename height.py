import sys

def findHeight(N):
    height = 1
    # N is number of growth cycles
    # if N is 1 it doubles, two it adds 1 
    for cycle in range(1, N+1):
        if cycle % 2 == 1:
            height = height  * 2
        else:
            height = height + 1
            
    return height

            
line_number = 0          
for line in sys.stdin:
    line = line.rstrip('\n')
    if line_number == 0:
        pass
    else:
        output = findHeight(line) + "\n"
        sys.stdout.write(output)
    line_number = line_number + 1

print findHeight(2)
print findHeight(3)
print findHeight(4)