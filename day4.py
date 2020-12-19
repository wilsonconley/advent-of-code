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
		data.append(x.replace("\n"," "))
	f.close()

	return data

def power(base, exp, tot=1):
	if exp > 0:
		tot *= base
		exp -= 1
		tot = power(base, exp, tot)
	return tot

class Passport():
	def __init__(self, line):
		self._fields = {
			"byr": "",
			"iyr": "",
			"eyr": "",
			"hgt": "",
			"hcl": "",
			"ecl": "",
			"pid": "",
			"cid": ""	
		}
		tmp = re.split(" ", line)
		tmp.remove("")
		for x in tmp:
			[key, value] = re.split(":", x)
			self._fields[key] = value

	def check_valid(self):
		valid = 1
		for x in self._fields.keys():
			if x != "cid":
				if self._fields[x] == "":
					valid = 0
		return valid

	def check_valid_2(self):
		valid = 1
		for x in self._fields.keys():
			tmp = self._fields[x]
			if x == "byr":
				if len(tmp) != 4 or any([c < "0" or c > "9" for c in tmp]) or int(tmp) < 1920 or int(tmp) > 2002:
					valid = 0
					print("byr: " + tmp)
			elif x == "iyr":
				if len(tmp) != 4 or any([c < "0" or c > "9" for c in tmp]) or int(tmp) < 2010 or int(tmp) > 2020:
					valid = 0
					print("iyr: " + tmp)
			elif x == "eyr":
				if len(tmp) != 4 or any([c < "0" or c > "9" for c in tmp]) or int(tmp) < 2020 or int(tmp) > 2030:
					valid = 0
					print("eyr: " + tmp)
			elif x == "hgt":
				num = list()
				units = ""
				for c in tmp:
					if c >= "0" and c <= "9":
						num.append(int(c))
					else:
						units += c
				height = 0
				if len(num) == 0:
					valid = 0
					print("hgt: " + tmp)
					return valid
				for i in range(0, len(num)):
					height += num[i] * power(10, len(num) - i - 1)
				if units == "cm":
					if height < 150 or height > 193:
						valid = 0
						print("hgt [cm]: " + tmp + " " + str(height))
				elif units == "in":
					if height < 59 or height > 76:
						valid = 0
						print("hgt [in]: " + tmp + " " + str(height))
				else:
					valid = 0
					print("hgt: " + tmp)
			elif x == "hcl":
				if len(tmp) != 7:
					valid = 0
					print("hcl: " + tmp)
				for c in range(0, len(tmp)):
					if c == 0:
						if tmp[c] != "#":
							valid = 0
							print("hcl: " + tmp)
					else:
						if not (tmp[c] >= "0" and tmp[c] <= "9") and not (tmp[c] >= "a" and tmp[c] <= "f"):
							valid = 0
							print("hcl: " + tmp)
			elif x == "ecl":
				choices = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
				if not tmp in choices:
					valid = 0
					print("ecl: " + tmp)
			elif x == "pid":
				if len(tmp) != 9:
					valid = 0
					print("pid: " + tmp)
				if any([c < "0" or c > "9" for c in tmp]):
					valid = 0
					print("pid: " + tmp)
		return valid

if __name__ == "__main__":
	data = read_file()
	all_pass = list()
	tmp = ""
	for x in data:
		if x == " ":
			all_pass.append(Passport(tmp))
			tmp = ""
		else:
			tmp = tmp + x

	num_valid = 0
	num_valid_2 = 0
	for x in all_pass:
		num_valid += x.check_valid()
		num_valid_2 += x.check_valid_2()

	print("Num valid = " + str(num_valid))
	print("Num valid 2 = " + str(num_valid_2))

