#!/usr/local/bin/python3

import os

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Inputs", os.path.basename(__file__).replace("py","txt"))

print("\nLoading File:")
print(filename + "\n")

data = list()
f = open(filename)
for x in f:
	data.append(int(x))
f.close()

print(data,end="\n\n")

# 2 numbers
product = list()
for i in range(0, len(data)):
	for j in range(0, len(data)):
		if j == i:
			continue
		if data[i] + data[j] == 2020:
			print("i = " + str(data[i]) + ", j = " + str(data[j]))
			product.append(data[i] * data[j])

print("\nProduct is: " + str(product) + "\n")

# 3 numbers
product = list()
for i in range(0, len(data)):
	for j in range(0, len(data)):
		for k in range(0, len(data)):
			if k == j or k == i or j == i:
				continue
			if data[i] + data[j] + data[k] == 2020:
				print("i = " + str(data[i]) + ", j = " + str(data[j]) + ", k = " + str(data[k]))
				product.append(data[i] * data[j] * data[k])

print("\nProduct is: " + str(product) + "\n")