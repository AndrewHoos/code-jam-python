#written by Andrew Hoos
# andrewhoos.com

import sys
import re


number_of_cases = int(sys.stdin.readline().strip())



for case in range(number_of_cases):
	credit_amount = int(sys.stdin.readline().strip())
	solution = [False]*(credit_amount+1)
	number_of_items = int(sys.stdin.readline().strip())
	items = sys.stdin.readline()
	item_values = re.split(" ",items)
	return_line = "Case #" +str(case+1)+": "
	# search for a pair
	for index2 in range(len(item_values)):
		# parse the item
		item_values[index2] = int(item_values[index2])
		# if item is more than credit
		if item_values[index2] > credit_amount:
			continue




		# search to see if opposite is found
		opposite_value = credit_amount-item_values[index2]
		if bool(solution[opposite_value]):
			for index1 in range(index2):
				if item_values[index1] == opposite_value:
					print(return_line + str(index1+1)+ " " + str(index2+1))
			#leave the search move to next case
			break
		else:
			solution[item_values[index2]]=True;






