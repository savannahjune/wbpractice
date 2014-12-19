# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def findIntegers(N):
    divisible_count = 0
    for character in N:
        N_int = int(character)
        if N_int != 0 and int(N) % N_int == 0:
            divisible_count = divisible_count + 1
    return divisible_count

            
line_number = 0          
for line in sys.stdin:
    line = line.rstrip('\n')
    if line_number == 0:
        pass
    else:
        output = str(findIntegers(line)) + "\n"
        sys.stdout.write(output)  
    line_number = line_number + 1