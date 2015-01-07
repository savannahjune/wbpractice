import sys

def fillCrossword():
	pass


class Dash(object):
	def __init__(self):
		

line_number = 0 
last_line = ''   
for line in sys.stdin:
    line = line.rstrip('\n')

    line_number = line_number + 1
    last_line = line

print last_line




'''
+-++++++++  
+-++++++++  
+-++++++++  
+-----++++  
+-+++-++++  
+-+++-++++  
+++++-++++  
++------++  
+++++-++++  
+++++-++++  
LONDON;DELHI;ICELAND;ANKARA  
'''