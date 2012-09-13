# written by Andrew Hoos
# andrewhoos.com



import sys
import re


def stringForChar(character):
	if(character == "\n"):
		return ""
	value = ord(character)-ord("a")

	if character == " ":
		return "0"
	if value <= ord("c") - ord("a"):
		return "2"*(value+1)
	if value <= ord("f") - ord("a"):
		return "3"*(value+ord("a")-ord("c"))
	if value <= ord("i") - ord("a"):
		return "4"*(value+ord("a")-ord("f"))
	if value <= ord("l") - ord("a"):
		return "5"*(value+ord("a")-ord("i"))
	if value <= ord("o") - ord("a"):
		return "6"*(value+ord("a")-ord("l"))
	elif value <= ord("s")-ord("a"):
		return "7"*(value+ord("a")-ord("o"))
	elif value <= ord("v")-ord("a"):
		return "8"*(value+ord("a")-ord("s"))
	elif value <= ord("z")-ord("a"):
		return "9"*(value+ord("a")-ord("v"))
	else:
		print("xxxxxx"+character)



cases = int(sys.stdin.readline())
for case in range(cases):
	line = sys.stdin.readline()
	return_string = "Case #"+str(case+1)+": "
	string_for_last_char = ""
	for char in line:
		string_for_current_char = stringForChar(char)
		try:
			if string_for_last_char[0] == string_for_current_char[0]:
				return_string = return_string + string_for_last_char + " "
			else:
				return_string = return_string + string_for_last_char
		except:
			return_string = return_string + string_for_last_char
		string_for_last_char = string_for_current_char



	return_string = return_string + string_for_last_char

	print(return_string)
