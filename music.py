#written by Andrew Hoos
# andrewhoos.com

import sys
import re


number_of_cases = int(sys.stdin.readline().strip())


for case in range(number_of_cases):

	songs = int(sys.stdin.readline().strip())

	song_list = []
	for song in range(songs):
		song_list.append(sys.stdin.readline().strip())

	print("Case #"+str(case+1)":")

	for i in range(len(song_list)):

		found = False
		for j in song_list[:i]+song_list[i+1:]
			if i in j:
				print(":(")





