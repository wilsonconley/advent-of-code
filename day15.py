#!/usr/local/bin/python3

import os
import re
import string
import numpy as np
import copy

def read_file():
	filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Inputs", os.path.basename(__file__).replace("py","txt"))

	print("Loading File:")
	print(filename)

	data = list()
	f = open(filename)
	for x in f:
		data.append(x.replace("\n",""))
	f.close()

	return data

if __name__ == "__main__":
	data = read_file()
	start_num = re.split(",", data[0])
	print(start_num)

	num_turn = 30000000
	all_num = list()
	for i in range(0, num_turn):
		# print(i)
		if i < len(start_num):
			tmp = int(start_num[i])
		else:
			last_num = all_num[-1]
			if all_num.count(last_num) == 1:
				tmp = 0
			else:
				idx = len(all_num) - 2
				while all_num[idx] != last_num:
					idx -= 1
				tmp = (i - 1) - idx
		all_num.append(tmp)
		# print(all_num)
		# print(tmp)
	print(all_num)