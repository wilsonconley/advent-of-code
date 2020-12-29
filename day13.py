#!/usr/local/bin/python3

# import os
# import re
# import string
# import numpy as np
# import copy

# def read_file():
# 	filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Inputs", os.path.basename(__file__).replace("py","txt"))

# 	print("Loading File:")
# 	print(filename)

# 	data = list()
# 	f = open(filename)
# 	for x in f:
# 		data.append(x.replace("\n",""))
# 	f.close()

# 	return data

# if __name__ == "__main__":
# 	data = read_file()
# 	print(data)

# 	# part 1
# 	time = int(data[0])
# 	bus_times = re.split(",", data[1])
# 	valid_bus = [int(x) for x in bus_times if x != "x"]
# 	early_time = copy.deepcopy(valid_bus)
# 	for i in range(0, len(valid_bus)):
# 		while early_time[i] < time:
# 			early_time[i] += valid_bus[i]
# 	differences = list()
# 	for i in range(0, len(early_time)):
# 		differences.append(early_time[i] - time)
# 	short = min(differences)
# 	idx = differences.index(short)
# 	bus_id = valid_bus[idx]
# 	total = bus_id * short

# 	print("answer = " + str(total))

# 	# part 2
# 	offsets = list()
# 	for i in range(0, len(bus_times)):
# 		if bus_times[i] != "x":
# 			offsets.append(i)


# 	# valid_bus = [5, 7, 8]
# 	# offsets = [3, 1, 6]

# 	valid_bus = valid_bus[1:]
# 	offsets = offsets[1:]

# 	print(valid_bus)
# 	print(offsets)

# 	N = 1
# 	for i in range(0, len(valid_bus)):
# 	# for i in range(1, len(valid_bus)):
# 		N *= valid_bus[i]
# 	print(N)

# 	summation = 0
# 	for i in range(0, len(valid_bus)):
# 	# for i in range(1, len(valid_bus)):
# 		b_i = offsets[i]
# 		N_i = N // valid_bus[i]
# 		f = N_i % valid_bus[i]
# 		x_i = 1
# 		print("b_i")
# 		print(b_i)
# 		print("N_i")
# 		print(N_i)
# 		print("f")
# 		print(f)
# 		print("x_i")
# 		print(x_i)
# 		while (f * x_i) % valid_bus[i] != 1:
# 			x_i += 1
# 			print(x_i)
# 		summation += b_i * N_i * x_i
# 		print("summation")
# 		print(summation)
# 	x = summation % N
# 	print("x = " + str(x))


# 	for i in range(0, len(valid_bus)):
# 		print("bus id = " + str(valid_bus[i]))
# 		print("offset = " + str(offsets[i]))
# 		tmp = x % valid_bus[i]
# 		print("x % bus id = " + str(tmp))


# 	# # part 2
# 	# offsets = list()
# 	# for i in range(0, len(bus_times)):
# 	# 	if bus_times[i] != "x":
# 	# 		offsets.append(i)

# 	# valid = False
# 	# tmp = 2000000000000000
# 	# while tmp % valid_bus[0] != 0:
# 	# 	tmp += 1
# 	# tmp -= valid_bus[0]
# 	# while not valid:
# 	# 	valid = True
# 	# 	tmp += valid_bus[0]
# 	# 	print(tmp)
# 	# 	for i in range(1, len(valid_bus)):
# 	# 		if (tmp + offsets[i]) % valid_bus[i] != 0:
# 	# 			valid = False
# 	# timestamp = tmp
# 	# print("t = " + str(timestamp))

# couldnt get patr 2

import math
import os
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "Inputs", os.path.basename(__file__).replace("py","txt")), "r") as file:
	lines = file.read().split()
	departure_time = int(lines[0])
	bus_ids = lines[1].split(",")
	working_bus_ids = [int(n) for n in bus_ids if n != "x"]

# Part 1
bus_time_waited = [(i, i - departure_time % i) for i in working_bus_ids]
closest_bus = min(bus_time_waited, key=lambda b: b[1])
print("Part 1:", math.prod(closest_bus))

# Part 2 - Used hints (found out the "Chinese Remainder Theorem" was required and researched it)

# All bus IDs are prime so all pairs of IDs will have a GCD of 1
# Therefore, the Chinese Remainder Theorem will work
def chinese_remainder_theorem(bus_ids):
	# If you're confused I would recommend watching this video:
	# https://youtu.be/zIFehsBHB8o

	# Create a dictionary of the following format:
	# key: bus_id
	# value: array containing various info
	# array[0] is timestamp offset
	# Equations used for array[1] onwards:
	# x ≅ b (mod n)
	# N is the product of all the 'n's (n₁ * n₂ * n₃...)
	# Nᵢ = N/nᵢ (i.e. the product of all the 'n's excluding nᵢ)
	# xᵢ ≅ (1/Nᵢ) (mod n) (i.e. modular inverse of Nᵢ mod n)
	# array[1] is the remainder (bᵢ)
	# array[2] is Niᵢ
	# array[3] is xᵢ

	# Only adds array[0]
	bus_id_info = {int(bus_id): [i] for i, bus_id in enumerate(bus_ids) if bus_id != "x"}

	id_product = math.prod(bus_id_info)

	# Adds array[1] onwards
	x = 0
	for bus_id in bus_id_info:
		info = bus_id_info[bus_id]
		offset = info[0]

		bi = (bus_id - offset) % bus_id
		info.append(bi)

		# Using floor division here means ni will be an integer instead of a float
		# When a float is greater than 2^53 then precision issues will occur
		# ni on its own isn't greater than 2^53 (at least in the puzzle input)
		# But x is so x must be an integer (which it will be if bi, ni, and xi are all integers)
		ni = id_product // bus_id
		info.append(ni)

		c = ni % bus_id
		xi = 1
		while (c * xi) % bus_id != 1:
			xi += 1
		info.append(xi)

		x += bi * ni * xi

	t = x % id_product

	return t

print("Part 2:", chinese_remainder_theorem(bus_ids))

