#!/usr/local/bin/python3

import os
import re

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

def power(base, exp, tot=1):
	if exp > 0:
		tot *= base
		exp -= 1
		tot = power(base, exp, tot)
	return tot

if __name__ == "__main__":
	data = read_file()

	seat = list()
	for x in data:
		# get row
		f_b = x[0:7]
		f_b = f_b.replace("F", "0")
		f_b = f_b.replace("B", "1")
		row = 0
		for bit in range(0, len(f_b)):
			if f_b[len(f_b)-bit-1] == "1":
				row += power(2, bit)
		
		# get col
		l_r = x[7:len(x)]
		l_r = l_r.replace("L", "0")
		l_r = l_r.replace("R", "1")
		col = 0
		for bit in range(0, len(l_r)):
			if l_r[len(l_r)-bit-1] == "1":
				col += power(2, bit)

		# get seat
		seat.append(row * 8 + col)

	# return max seat number
	print("max seat = " + str(max(seat)))

	# get your seat number
	seat.sort()
	for x in range(min(seat), max(seat) + 1):
		if x not in seat:
			print("missing seat: " + str(x))

