#written by Andrew Hoos
# andrewhoos.com

import sys
import re


number_of_cases = int(sys.stdin.readline().strip())


vowels = ['a','A','e','E','i','I','o','O','u','U']
y = ['y','Y']
for case in range(number_of_cases):

	line = sys.stdin.readline().strip()

	if line[len(line)-1] in vowels:
		sys.stdout.write("Case #"+str(case+1)+": " + line + " is ruled by a queen.\n")
	elif line[len(line)-1] in y:
		sys.stdout.write("Case #"+str(case+1)+": " + line + " is ruled by nobody.\n")
	else:
		sys.stdout.write("Case #"+str(case+1)+": " + line + " is ruled by a king.\n")
