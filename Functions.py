#==================================================================
#							     Loops
#==================================================================



def getInfo():
	global a, b
	a = int(input('Please enter the first number in the range\nFirst'))
	b = int(input('Please enter the second number in the range\nSecond'))
	return a, b

def loopIt(first, second):
# see if you can use a = 0 here in args
	for i in range(a, b):
		print('i is now {}'.format(i))

getInfo()
loopIt(a, b)

















