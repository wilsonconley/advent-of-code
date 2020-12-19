#!/usr/local/bin/python3

import os
import re

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Inputs", os.path.basename(__file__).replace("py","txt"))

print("\nLoading File:")
print(filename + "\n")

data = list()
f = open(filename)
for x in f:
	data.append(x.replace("\n",""))
f.close()

print(data,end="\n\n")

policy = list()
password = list()
for line in data:
	tmp = re.split(":", line)
	policy.append(tmp[0])
	password.append(tmp[1])

min_count = list()
max_count = list()
char_search = list()
for x in range(0, len(policy)):
	tmp = re.split(" ", policy[x])
	tmp2 = re.split("-", tmp[0])
	min_count.append(int(tmp2[0]))
	max_count.append(int(tmp2[1]))
	char_search.append(tmp[1])

valid = list()
for x in range(0, len(min_count)):
	num = len(re.findall(char_search[x], password[x]))
	if num >= min_count[x] and num <= max_count[x]:
		valid.append(1)

print("num valid = " + str(len(valid)))

valid = list()
for x in range(0, len(min_count)):
	a = password[x][min_count[x]]
	b = password[x][max_count[x]]
	# print("a = " + a + ", b = " + b + ", search = " + char_search[x])
	print(password[x])
	if (a == char_search[x] and b != char_search[x]) or (a != char_search[x] and b == char_search[x]):
		valid.append(1)

print("num valid (2) = " + str(len(valid)))
