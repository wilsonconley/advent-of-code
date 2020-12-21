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

def run_scenario(data):
	# print("run scenario on: ")
	# print(data)
	valid = True
	run = np.zeros(len(data))
	instruction = 0
	while (instruction < len(data) and run[instruction] == 0):
		# print("\tLine " + str(instruction))
		run[instruction] = 1
		x = data[instruction]
		if x[0:3] == "acc":
			instruction += 1
		elif x[0:3] == "jmp":
			instruction += int(x[4:])
		else:
			instruction += 1
		# print("\tNew instrction = " + str(instruction))
		if instruction < len(data) and run[instruction] == 1:
			# print("run[instruction] = " + str(run[instruction]))
			valid = False
	return valid

if __name__ == "__main__":
	data = read_file()

	# part 1
	run = np.zeros(len(data))
	count = 0
	instruction = 0
	while (run[instruction] == 0):
		run[instruction] = 1
		x = data[instruction]
		if x[0:3] == "acc":
			# print("adding: " + str(int(x[4:])))
			count += int(x[4:])
			instruction += 1
		elif x[0:3] == "jmp":
			instruction += int(x[4:])
		else:
			instruction += 1

	print("count = " + str(count))

	# part 2
	fixed = False
	count = 0
	instruction = 0
	run = np.zeros(len(data))
	while instruction < len(data):
		print("Line " + str(instruction))
		if run[instruction] == 1:
			print(data[instruction] + "already run")
			break
		run[instruction] = 1
		x = data[instruction]
		if x[0:3] == "acc":
			count += int(x[4:])
			instruction += 1
		elif x[0:3] == "jmp":
			if not fixed:
				tmp = copy.deepcopy(data)
				tmp[instruction] = tmp[instruction].replace("jmp", "nop")
				if run_scenario(tmp):
					print("changing line " + str(instruction) + " from " + data[instruction] + " to " + tmp[instruction])
					data = tmp
					fixed = True
					instruction += 1
				else:
					instruction += int(x[4:])
			else:
				instruction += int(x[4:])
		else:
			if not fixed:
				tmp = copy.deepcopy(data)
				tmp[instruction] = tmp[instruction].replace("nop", "jmp")
				if run_scenario(tmp):
					print("changing line " + str(instruction) + " from " + data[instruction] + " to " + tmp[instruction])
					data = tmp
					fixed = True
					instruction += int(x[4:])
				else:
					instruction += 1
			else:
				instruction += 1

	print("count = " + str(count))