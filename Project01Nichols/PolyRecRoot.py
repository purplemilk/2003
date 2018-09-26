#Katy M. Nichols
#Project 01
#2003-L2

import math
import itertools
from Point import Point
from Polygon import Polygon
from Rectangle import Rectangle

in_file = open('project01data.txt', 'r')

line = in_file.readlines()

i=0

while i<len(line):
	if line[i].split()[0]=="R":
		i = i+1
		list = []

		for j in range(4):
			point = Point(float(line[i].split()[0]), float(line[i].split()[1]))
			list.append(point)
			i = i+1

		myrectangle = Rectangle(list)

		print ("the four vertices of the myrectangle are ...")
		print(myrectangle)
		print ("the length of myrectangle is ... ")
		print(myrectangle.length)
		print ("the width of myrectangle is ... ")
		print(myrectangle.width)
		print ("the perimeter of myrectangle is ... ")
		print(myrectangle.perimeter())
		print ("the area of myrectangle is ... ")
		print(myrectangle.area())

	else:
		vertices = int(line[i].split()[1])
		i = i+1
		list = []

		for j in range(vertices):
			point = Point(float(line[i].split()[0]), float(line[i].split()[1]))
			list.append(point)
			i = i+1

		mypolygon = Polygon(list)

		print ("the four vertices of the mypolygon are ...")
		print(mypolygon)
		print ("the perimeter of mypolygon is ... ")
		print(mypolygon.perimeter())
		print ("the area of mypolygon is ... ")
		print(mypolygon.area())
			



