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
	# print(data)

	# part 1
	for idx in range(25, len(data)):
		target = int(data[idx])
		numbers = [int(data[i]) for i in range(idx - 25, idx)]
		valid = False
		for i in range(0, len(numbers)):
			for j in range(0, len(numbers)):
				if i != j:
					if numbers[i] + numbers[j] == target:
						valid = True
		if not valid:
			print("Idx = " + str(idx) + ", Number = " + str(target) + " is invalid")
			break

	# part 2
	found = False
	for i in range(0, len(data)):
		stop = i + 1
		iterate = True
		while iterate and stop < len(data):
			total_sum = sum([int(data[j]) for j in range(i, stop + 1)])
			if total_sum == target:
				print(total_sum)
				print("start = " + str(i) + ", stop = " + str(stop))
				print(data[i] + " + " + data[stop] + " = " + str(int(data[i]) + int(data[stop])))
				iterate = False
				found = True
			elif total_sum > target:
				iterate = False
			else:
				stop += 1
		if found:
			break

	numbers = [int(data[j]) for j in range(i, stop + 1)]
	small = min(numbers)
	large = max(numbers)
	final = small + large
	print("Small = ")
	print(small)
	print("Large = ")
	print(large)
	print("Sum = ")
	print(final)

