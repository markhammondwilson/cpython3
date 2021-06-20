import sys, os
try:
	f = sys.argv[1]
except:
	print('\033[91mError: not enough arguments\033[0m')
	quit()
full_path = os.path.abspath(f)
if os.path.isfile(f):
	if os.path.isdir('/volumes/CIRCUITPY'):
		codepy = open('/volumes/CIRCUITPY/code.py', 'a')
		open('/volumes/CIRCUITPY/code.py', 'w').write('')
		for i in open(f, 'r').readlines():
			codepy.write(i)
	else:
		print('\033[91mCannot find your CIRCUITPY drive. Try double-tapping the reset button and then pressing it again.\033[0m')
else:
	print('\033[91mERROR: cannot find file\033[0m')
