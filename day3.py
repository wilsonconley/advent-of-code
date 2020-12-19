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

c = 0
hit = 0
for x in range(0, len(data)):
	if c >= len(data[x]):
		c = c % len(data[x])
	if data[x][c] == "#":
		hit += 1

	print("r = " + str(x) + ", c = " + str(c))

	c += 3

print("hit = " + str(hit))

# down 1, right 1
all_hit = list()
c = 0
hit = 0
for x in range(0, len(data)):
	if c >= len(data[x]):
		c = c % len(data[x])
	if data[x][c] == "#":
		hit += 1
	c += 1
all_hit.append(hit)

# down 1, right 3
c = 0
hit = 0
for x in range(0, len(data)):
	if c >= len(data[x]):
		c = c % len(data[x])
	if data[x][c] == "#":
		hit += 1
	c += 3
all_hit.append(hit)

# down 1, right 5
c = 0
hit = 0
for x in range(0, len(data)):
	if c >= len(data[x]):
		c = c % len(data[x])
	if data[x][c] == "#":
		hit += 1
	c += 5
all_hit.append(hit)

# down 1, right 7
c = 0
hit = 0
for x in range(0, len(data)):
	if c >= len(data[x]):
		c = c % len(data[x])
	if data[x][c] == "#":
		hit += 1
	c += 7
all_hit.append(hit)

# down 2, right 1
c = 0
hit = 0
for x in range(0, len(data)):
	if x % 2 > 0:
		continue
	if c >= len(data[x]):
		c = c % len(data[x])
	if data[x][c] == "#":
		hit += 1
	c += 1
all_hit.append(hit)

print(all_hit)

product = 1
for x in all_hit:
	product *= x

print("total product = " + str(product))
