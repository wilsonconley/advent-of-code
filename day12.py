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

class Ferry():
	"""docstring for Ferry"""
	def __init__(self, direction):
		self._facing = direction
		self._x = 0
		self._y = 0

	def _rotate(self, direction, degrees):
		rot = ["N", "E", "S", "W"]
		rot_idx = rot.index(self._facing)
		rot_apply = degrees / 90
		if direction == "R":
			self._facing = rot[int((rot_idx + rot_apply) % len(rot))]
		else:
			self._facing = rot[int((rot_idx - rot_apply) % len(rot))]

	def _move(self, direction, amount):
		if direction == "N":
			self._y += amount
		elif direction == "E":
			self._x += amount
		elif direction == "S":
			self._y -= amount
		elif direction == "W":
			self._x -= amount
		elif direction == "F":
			self._move(self._facing, amount)

class FerryWaypoint():
	"""docstring for Ferry"""
	def __init__(self):
		self._x = 0
		self._y = 0
		self._waypoint_x = 10
		self._waypoint_y = 1

	def _rotate(self, direction, degrees):
		if degrees == 270:
			if direction == "R":
				direction = "L"
			else:
				direction = "R"
			degrees = 90

		if degrees == 90:
			if direction == "R":
				new_x = self._waypoint_y
				new_y = -self._waypoint_x
			else:
				new_x = -self._waypoint_y
				new_y = self._waypoint_x
		elif degrees == 180:
			new_x = -self._waypoint_x
			new_y = -self._waypoint_y
		else:
			print("Not defined for " + str(degrees))

		self._waypoint_x = new_x
		self._waypoint_y = new_y

	def _move_waypoint(self, direction, amount):
		if direction == "N":
			self._waypoint_y += amount
		elif direction == "E":
			self._waypoint_x += amount
		elif direction == "S":
			self._waypoint_y -= amount
		elif direction == "W":
			self._waypoint_x -= amount

	def _move(self, amount):
		self._x += self._waypoint_x * amount
		self._y += self._waypoint_y * amount

if __name__ == "__main__":
	data = read_file()

	# part 1
	f = Ferry("E")
	for i in data:
		# print("==========================================")
		# print(i)
		direction = i[0]
		amount = int(i[1:])
		if direction == "L" or direction == "R":
			# print(f._facing + " -> ", end="")
			f._rotate(direction, amount)
			# print(f._facing)
		else:
			# if direction == "F":
			# 	print("facing " + f._facing)
			# print("(" + str(f._x) + ", " + str(f._y) + ") -> ", end="")
			f._move(direction, amount)
			# print("(" + str(f._x) + ", " + str(f._y) + ")")
	print("Final (x, y) = (" + str(f._x) + ", " + str(f._y) + ")")
	print("Manhattan distance = " + str(abs(f._x) + abs(f._y)))

	# part 2
	f = FerryWaypoint()
	for i in data:
		# print("==========================================")
		# print(i)
		direction = i[0]
		amount = int(i[1:])
		if direction == "L" or direction == "R":
			# print("(" + str(f._waypoint_x) + ", " + str(f._waypoint_y) + ") -> ", end="")
			f._rotate(direction, amount)
			# print("(" + str(f._waypoint_x) + ", " + str(f._waypoint_y) + ")")
		else:
			if direction == "F":
				# print("(" + str(f._x) + ", " + str(f._y) + ") -> ", end="")
				f._move(amount)
				# print("(" + str(f._x) + ", " + str(f._y) + ")")
			else:
				# print("(" + str(f._waypoint_x) + ", " + str(f._waypoint_y) + ") -> ", end="")
				f._move_waypoint(direction, amount)
				# print("(" + str(f._waypoint_x) + ", " + str(f._waypoint_y) + ")")
	print("Final (x, y) = (" + str(f._x) + ", " + str(f._y) + ")")
	print("Manhattan distance = " + str(abs(f._x) + abs(f._y)))
