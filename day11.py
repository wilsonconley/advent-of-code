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
		data.append(list(x.replace("\n","")))
	f.close()

	return data

def apply_rules(data):
	tmp = copy.deepcopy(data)
	for i in range(0, len(tmp)):
		for j in range(0, len(tmp[i])):
			if tmp[i][j] == "L" and num_occupied(data, i, j) == 0:
				tmp[i][j] = "#"
			if tmp[i][j] == "#" and num_occupied(data, i, j) >= 4:
				tmp[i][j] = "L"
	return tmp

def num_occupied(data, row, col):
	row_check = [row]
	if row > 0:
		row_check.append(row - 1)
	if row < len(data) - 1:
		row_check.append(row + 1)

	col_check = [col]
	if col > 0:
		col_check.append(col - 1)
	if col < len(data[0]) - 1:
		col_check.append(col + 1)

	count = 0
	for r in row_check:
		for c in col_check:
			if r == row and c == col:
				continue
			if data[r][c] == "#":
				count += 1

	return count

def apply_rules_2(data):
	tmp = copy.deepcopy(data)
	for i in range(0, len(tmp)):
		for j in range(0, len(tmp[i])):
			if tmp[i][j] == "L" and num_occupied_distance(data, i, j) == 0:
				tmp[i][j] = "#"
			if tmp[i][j] == "#" and num_occupied_distance(data, i, j) >= 5:
				tmp[i][j] = "L"
	return tmp

def num_occupied_distance(data, row, col):
	# check each of 8 directions
	count = 0
	count += check_direction(data, row, col, 0, -1)  # left
	count += check_direction(data, row, col, 0, 1)  # right
	count += check_direction(data, row, col, 1, 0)  # up
	count += check_direction(data, row, col, -1, 0)  # down
	count += check_direction(data, row, col, 1, -1)  # left - up
	count += check_direction(data, row, col, -1, -1)  # left - down
	count += check_direction(data, row, col, 1, 1)  # right - up
	count += check_direction(data, row, col, -1, 1)  # right - down

	return count

def check_direction(data, r, c, r_shift, c_shift):
	found = 0
	r += r_shift
	c += c_shift
	while (r >= 0 and c >= 0 and r < len(data) and c < len(data[0])):
		if data[r][c] == "#":
			found = 1
			break
		elif data[r][c] == "L":
			break
		r += r_shift
		c += c_shift
	return found

if __name__ == "__main__":
	data = read_file()
	print(data)

	# apply til fixed
	count = 0
	max_count = 1000
	run = True
	while run and count < max_count:
		run = False
		print("data:")
		for i in data:
			print(i)
		new_data = apply_rules(data)
		print("new_data:")
		for i in new_data:
			print(i)
		for i in range(0, len(data)):
			for j in range(0, len(data[i])):
				if data[i][j] != new_data[i][j]:
					print("not equal at " + str(i) + ", " + str(j))
					run = True
					break
			if run:
				break
		data = new_data
		print(count)
		count += 1


	num = 0
	for i in data:
		num += i.count("#")
	print("Total occupied = " + str(num))

	print("================================================================")

	# part 2
	data = read_file()
	print(data)

	count = 0
	max_count = 1000
	run = True
	while run and count < max_count:
		run = False
		print("data:")
		for i in data:
			print(i)
		new_data = apply_rules_2(data)
		print("new_data:")
		for i in new_data:
			print(i)
		for i in range(0, len(data)):
			for j in range(0, len(data[i])):
				if data[i][j] != new_data[i][j]:
					print("not equal at " + str(i) + ", " + str(j))
					run = True
					break
			if run:
				break
		data = new_data
		print(count)
		count += 1


	num = 0
	for i in data:
		num += i.count("#")
	print("Total occupied = " + str(num))



	# new_data = apply_rules(data)
	# print(new_data)
	# while any([new_data[i][j] != data[i][j] for i in range(0, len(data)) for j in range(0, len(data[i]))]):
	# 	data = copy.deepcopy(new_data)
	# 	new_data = apply_rules(data)
	# 	print(new_data)
	# 	count += 1
	# 	print(count)
