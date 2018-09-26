#Katy M. Nichols
#Project 01
#2003-L2

import math
import itertools
from Point import Point

class Polygon(object):

	def __init__(self, list_points):
		self.vertices= list_points

	def translate(self, a = 0.0, b = 0.0):
		for p in self.vertices:
			Point.translate(p,a,b)

	def scale(self, sx = 0.0, sy = 0.0):
		for p in self.vertices:
			Point.scale(p,sx,sy)

	def rotate(self, theta_in_degrees = 0.0):
		for p in self.vertices:
			Point.rotate(p,theta_in_degrees)

	def __str__(self):
		s=""
		for p in self.vertices:
		# s=s+" "+str(p.x)+" "+str(p.y)+"\n"
			s=s+" "+"{:.2f}".format(p.x)+" "+"{:.2f}".format(p.y)+"\n"
		return(s)

	#####USING ITERTOOLS.CYCLE

	def perimeter(self):
	 #convert a list of points into a list of distances
		print ("Using Polygon's perimeter routine")
		distances = []
		circular_buffer = itertools.cycle(self.vertices)
		previous_point = next(circular_buffer)
		for i in range(len(self.vertices)):
			point = next(circular_buffer)
			d = point.distance(previous_point)
			distances.append(d)
			previous_point = point
		return "{:.2f}".format(sum(distances))

	def area(self):
		s = []		
		for i in range(len(self.vertices)):
			if i==(len(self.vertices)-1):
				p = self.vertices[i].x*self.vertices[0].y - self.vertices[i].y*self.vertices[0].x
			else:
				p = self.vertices[i].x*self.vertices[i+1].y - self.vertices[i].y*self.vertices[i+1].x
				s.append(p)
		return "{:.2f}".format(abs(sum(s))/2)


