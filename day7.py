#!/usr/local/bin/python3

import os
import re
import string

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

class Rule():
	def __init__(self, line):
		self._outer = ""
		self._inner = list()
		[a, b] = re.split(" contain ", line.replace(".", ""))
		a = a.replace(" bags", "")
		a = a.replace(" bag", "")
		b = b.replace(" bags", "")
		b = b.replace(" bag", "")
		self._outer = a
		tmp = re.split(",", b)
		for x in tmp:
			count = re.findall("\d+", x)
			if len(count) == 0:
				self._inner = ""
				return
			count = count[0]
			color = re.findall("\D+ \D+", x)
			color = color[0]
			space_count = 0
			start_space = color[0]
			while start_space == " ":
				space_count += 1
				start_space = color[space_count]
			color = color[space_count:]
			self._inner.append({"color": color, "count": int(count)})

def search_rules(all_rules, bag):
	all_outer = list()
	for idx in range(0, len(all_rules)):
	# for idx in range(0, 1):
		x = all_rules[idx]
		if x._outer == bag:
			continue
		# print("Outer = " + x._outer)
		# print(str(len(x._inner)))
		for i in x._inner:
			# print("Inner: " + i["color"])
			all_colors = recursive_search(all_rules, i["color"], all_colors=[i["color"]])
			# print("all_colors = ")
			# print(all_colors)
			if bag in all_colors:
				all_outer.append(x._outer)
				# print("found: " + x._outer)
				break
	return all_outer


def recursive_search(all_rules, color, all_colors):
	for x in all_rules:
		if x._outer == color:
			if x._inner == "":
				return all_colors
			for i in x._inner:
				# print("append " + i["color"])
				if i["color"] not in all_colors:
					all_colors.append(i["color"])
				# print(all_colors)
				all_colors = recursive_search(all_rules, i["color"], all_colors=all_colors)
				# print(all_colors)
	return all_colors

def count_bags(all_rules, bag, multiplier, count):
	orig_multiplier = multiplier
	for x in all_rules:
		if x._outer == bag:
			if x._inner == "":
				return count
			for i in x._inner:
				count += orig_multiplier * i["count"]
				multiplier = orig_multiplier * i["count"]
				count = count_bags(all_rules, i["color"], multiplier, count)
	return count

if __name__ == "__main__":
	data = read_file()

	all_rules = list()
	for x in data:
		all_rules.append(Rule(x))
		# print(all_rules[-1]._outer)
		# print(all_rules[-1]._inner)

	bag = "shiny gold"
	all_outer = search_rules(all_rules, bag)
	all_outer = list(set(all_outer))
	# print("all_outer: ")
	# print(all_outer)
	print("num outer = " + str(len(all_outer)))

	# part 2
	count = count_bags(all_rules, bag, 1, 0)
	print("count of bags = " + str(count))
