#written by Andrew Hoos
# andrewhoos.com

import sys
import re

cases = int(sys.stdin.readline())
for case in range(cases):
	line = sys.stdin.readline().strip()
	line = re.split(" ",line)
	line.reverse()
	line = " ".join(line)
	print("Case #"+str(case+1)+": "+line)
