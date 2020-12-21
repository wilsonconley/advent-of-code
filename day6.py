#!/usr/local/bin/python3

import os
import re
import string

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

	all_sum = 0
	selected = list()
	for x in data:
		if x == "":
			all_sum += len(selected)
			selected = list()
		else:
			for c in x:
				if c not in selected:
					selected.append(c)
	if len(selected) > 0:
		all_sum += len(selected)

	print("Total sum (any) = " + str(all_sum))

	all_sum = 0
	selected = list()
	for x in data:
		if x == "":
			for c in string.ascii_lowercase:
				valid = 1
				for line in selected:
					if c not in line:
						valid = 0
				if valid == 1:
					all_sum += 1
			selected = list()
		else:
			selected.append(x)

	for c in string.ascii_lowercase:
		valid = 1
		for line in selected:
			if c not in line:
				valid = 0
		if valid == 1:
			all_sum += 1
		
	print("Total sum (all) = " + str(all_sum))