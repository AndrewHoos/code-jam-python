#written by Andrew Hoos
# andrewhoos.com

import sys
import re


number_of_cases = int(sys.stdin.readline().strip())


for case in range(number_of_cases):

	line = sys.stdin.readline()
	original_line = ""
	for char in line:
		if(char == 'y'):
			original_line +='a'
		elif(char == 'n'):
			original_line +='b'
		elif(char == 'f'):
			original_line +='c'
		elif(char == 'i'):
			original_line +='d'
		elif(char == 'c'):
			original_line +='e'
		elif(char == 'w'):
			original_line +='f'
		elif(char == 'l'):
			original_line +='g'
		elif(char == 'b'):
			original_line +='h'
		elif(char == 'k'):
			original_line +='i'
		elif(char == 'u'):
			original_line +='j'
		elif(char == 'o'):
			original_line +='k'
		elif(char == 'm'):
			original_line +='l'
		elif(char == 'x'):
			original_line +='m'
		elif(char == 's'):
			original_line +='n'
		elif(char == 'e'):
			original_line +='o'
		elif(char == 'v'):
			original_line +='p'
		elif(char == 'z'):
			original_line +='q'
		elif(char == 'p'):
			original_line +='r'
		elif(char == 'd'):
			original_line +='s'
		elif(char == 'r'):
			original_line +='t'
		elif(char == 'j'):
			original_line +='u'
		elif(char == 'g'):
			original_line +='v'
		elif(char == 't'):
			original_line +='w'
		elif(char == 'h'):
			original_line +='x'
		elif(char == 'a'):
			original_line +='y'
		elif(char == 'q'):
			original_line +='z'
		elif(char == ' '):
			original_line +=' '
	sys.stdout.write('Case #' + str(case+1) + ': ' + str(original_line) + '\n')







