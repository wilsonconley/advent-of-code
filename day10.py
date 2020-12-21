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

	# get all adapters and sort
	adapters = [int(i) for i in data]
	adapters.append(max(adapters) + 3)
	adapters.append(0)
	adapters.sort()

	# get number of 1 and 3 difference steps
	difference = list()
	for i in range(0, len(adapters) - 1):
		difference.append(adapters[i + 1] - adapters[i])
	print("1 diff = " + str(difference.count(1)))
	print("2 diff = " + str(difference.count(2)))	
	print("3 diff = " + str(difference.count(3)))
	product = difference.count(1) * difference.count(3)
	print("Product = " + str(product))

	# get number of consecutive 1 step differences in between 3 step diffs
	# these consecutive sets of 1 step differneces can be combined
	combos = list()
	start = 0
	for i in range(0, len(difference)):
		if difference[i] == 3:
			if i == start:
				start += 1
			else:
				length = i - start
				combos.append(length)
				start = i + 1

	# calculate total number of combos based upon length of consecutive 1 step differences
	total = 1
	for i in combos:
		if i == 1:
			val = 1
		elif i == 2:
			val = 2
		elif i == 3:
			val = 4
		elif i == 4:
			val = 7
		elif i == 5:
			val = 13
		else:
			print('Value not defined for ' + str(i))
		total *= val

	print("All differences")
	print(difference)

	print("Length of combinable step differences")
	print(combos)

	print("Total combinations =")
	print(total)
	
