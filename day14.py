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

def dec_2_bin(val):
	binary = list()
	bit = 0
	max_bit = 36
	if val > np.power(2, max_bit - 1):
		print("NUM TOO BIG")
	for b in range(max_bit - 1, -1, -1):
		if val >= np.power(2, b):
			binary.append("1")
			val -= np.power(2, b)
		else:
			binary.append("0")
	return binary

def bin_2_dec(bin_str):
	binary = bin_str[::-1]
	decimal = 0
	for i in range(0, len(binary)):
		decimal += int(binary[i]) * np.power(2, i)
	return decimal

if __name__ == "__main__":
	data = read_file()

	# part 1
	mem = dict()
	mask = ""
	for i in data:
		[cmd, val] = re.split(" = ", i)
		if cmd == "mask":
			mask = list(val)
		else:
			num = dec_2_bin(int(val))
			loc = re.findall("\d", cmd)
			write_loc = ""
			for j in loc:
				write_loc += str(j)
			val_apply = list()
			for j in range(0, len(mask)):
				if mask[j] == "X":
					val_apply.append(num[j])
				else:
					val_apply.append(mask[j])
			mem[write_loc] = val_apply
	count = 0
	for i in mem:
		count += bin_2_dec(mem[i])
	print("part 1")
	print(count)

	# part 2
	mem = dict()
	mask = ""
	for i in data:
		[cmd, val] = re.split(" = ", i)
		if cmd == "mask":
			mask = list(val)
		else:
			num = int(val)

			loc = re.findall("\d", cmd)
			tmp_loc = ""
			for j in loc:
				tmp_loc += str(j)
			loc = dec_2_bin(int(tmp_loc))

			loc_apply = list()
			for j in range(0, len(mask)):
				if mask[j] == "0":
					loc_apply.append(loc[j])
				else:
					loc_apply.append(mask[j])
			# print(loc_apply)

			last_index = 0
			index = list()
			for j in range(0, loc_apply.count("X")):
				index.append(loc_apply.index("X", last_index))
				last_index = loc_apply.index("X", last_index) + 1
			
			all_loc = list()
			max_num = np.power(2, len(index))
			for j in range(0, max_num):
				floating = dec_2_bin(j)
				floating = floating[len(floating) - len(index):]
				tmp_loc = copy.deepcopy(loc_apply)
				for k in range(0, len(index)):
					tmp_loc[index[k]] = floating[k]
				all_loc.append(bin_2_dec(tmp_loc))
			# print(all_loc)

			for j in all_loc:
				mem[str(j)] = num

	count = 0
	for i in mem:
		count += mem[i]
	print("part 2")
	print(count)



