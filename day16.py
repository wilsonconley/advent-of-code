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

def check_value(value, fields):
	valid = False
	for i in fields:
		for j in fields[i]:
			if value >= j["min"] and value <= j["max"]:
				valid = True
				break
		if valid:
			break

	return valid

def check_valid_lengths(rule_loc):
	valid = True
	for i in rule_loc["loc"]:
		if len(i) == 0:
			valid = False
			break
	return valid

def update_locs(rule_loc, loc_remove):
	# print("in func")
	# print(rule_loc)
	# print(loc_remove)
	for i in range(0, len(rule_loc["loc"])):
		# print(rule_loc["loc"][i])
		# print(loc_remove)
		# print(rule_loc["loc"][i].count(loc_remove))
		if loc_remove in rule_loc["loc"][i]:
			rule_loc["loc"][i].remove(loc_remove)
	# print(rule_loc)
	# print("end func")

def find_min(rule_loc):
	min_length = 9999999999
	for i in range(0, len(rule_loc["loc"])):
		if (i == 0 or len(rule_loc["loc"][i]) < min_length) and len(rule_loc["loc"][i]) > 0:
			min_length = len(rule_loc["loc"][i])
			# rule = rule_loc["rule"][i]
			rule = i
	return rule

if __name__ == "__main__":
	data = read_file()

	# get data
	fields = dict()
	for i in data:
		if len(i) == 0:
			break
		rules = list(range(0, 2))
		[key, value] = re.split(": ", i)
		[rules[0], rules[1]] = re.split(" or ", value)
		fields[key] = list()
		for j in rules:
			[r_min, r_max] = re.split("-", j)
			fields[key].append({"min": int(r_min), "max": int(r_max)})

	# part 1
	start = False
	invalid_values = list()
	valid_tickets = list()
	for i in data:
		if len(re.findall("nearby tickets", i)):
			start = True
			continue
		if start:
			all_val = [int(j) for j in re.split(",", i)]
			all_valid = True
			for j in all_val:
				valid = check_value(j, fields)
				if not valid:
					all_valid = False
					invalid_values.append(j)
			if all_valid:
				valid_tickets.append(i)

	print(invalid_values)
	print("sum = " + str(sum(invalid_values)))

	# part 2
	# print(valid_tickets)
	rule_loc = {"rule": list(), "loc": list()}
	for rule in fields:
		# print(rule)
		# print(fields[rule])
		all_loc = list(range(0, len(fields.keys())))
		loc = copy.deepcopy(all_loc)
		for ticket in valid_tickets:
			tmp = [int(i) for i in re.split(",", ticket)]
			for i in all_loc:
				if not ((tmp[i] >= fields[rule][0]["min"] and tmp[i] <= fields[rule][0]["max"]) or (tmp[i] >= fields[rule][1]["min"] and tmp[i] <= fields[rule][1]["max"])):
					loc.remove(i)
		# print(loc)
		rule_loc["rule"].append(rule)
		rule_loc["loc"].append(loc)

	# print(rule_loc)
	# for i in range(0, len(rule_loc["loc"])):
	# 	print(rule_loc["loc"][i])

	truth = {"rule": list(), "loc": list()}
	done = False
	while not done:
		min_idx = find_min(rule_loc)
		# print(min_idx)
		# print(rule_loc["rule"][min_idx])
		# print(rule_loc["loc"][min_idx])
		# print("before")
		# print(rule_loc["loc"])
		truth["rule"].append(rule_loc["rule"][min_idx])
		truth["loc"].append(copy.deepcopy(rule_loc["loc"][min_idx]))
		update_locs(rule_loc, rule_loc["loc"][min_idx][0])
		# print("after")
		# print(rule_loc["loc"])
		
		if len(truth["rule"]) == len(rule_loc["rule"]):
			done = True

	# print(truth)

	start = False
	for i in data:
		if "your ticket" in i:
			start = True
			continue
		if start:
			ticket = re.split(",", i)
			break
	# print(ticket)
	vals = list()
	for i in range(0, len(truth["rule"])):
		if "departure" in truth["rule"][i]:
			vals.append(int(ticket[truth["loc"][i][0]]))

	# print(vals)

	print("part 2: " + str(np.prod(vals)))








