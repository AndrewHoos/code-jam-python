#written by Andrew Hoos
# andrewhoos.com

import sys
import re


number_of_cases = int(sys.stdin.readline().strip())


for case in range(number_of_cases):

	line = sys.stdin.readline().strip()
	split_line = line.split(" ")
	unique_scores = int(split_line[1])
	minimum_score = int(split_line[2])

	#print("unique " +str(unique_scores))
	#print("minimum " +str(minimum_score))
	sure = 0
	possible = 0

	for score in range(3,len(split_line)):

		if int(split_line[score]) >= 3 * minimum_score - 2:
			sure = sure + 1
		elif int(split_line[score]) >= 3 * minimum_score - 4:
			if int(split_line[score]) >= minimum_score:
				possible = possible + 1

	#print(sure)
	#print(possible)

	max_possible = sure

	if possible >= unique_scores:
		max_possible = max_possible + unique_scores
	else:
		max_possible = max_possible + possible

	sys.stdout.write("Case #" + str(case+1) + ": "+str(max_possible)+ "\n")



