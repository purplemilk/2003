#Katy M. Nichols
#Project 01
#2003-L2

from Polygon import Polygon

class Rectangle(Polygon):

	def __init__(self, list):
		super(Rectangle,self).__init__(list)
		# self.length=6.0 this is the original code
		# self.width=4.0 this is the original code
		self.length = list[0].distance(list[1])
		self.width = list[1].distance(list[2])

	def perimeter(self):
		print ("Using Rectangle's perimeter routine")
		return 2*self.length+2*self.width

	def area(self):
		print ("Using Rectangle's area routine")
		return self.length*self.width
