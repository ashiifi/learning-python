"""
Intro to object oriented programming

#basic classes with attributes
#methods, instances, objects
"""

class Circle1(object):
	x0 = 1
	y0 = 2
	radius = 5

#another basic class with attributes and two methods
class Circle2(object):
	x0 = 1
	y0 = 2
	radius = 5
	pi = 3.14

	#first method:
	def area(self):
		return self.pi*self.radius**2

	#second method:
	def implicit_equation(self):
		return "(x-%f)^2+(y-%f)^2 = %f^2" % (self.x0, self.y0, self.radius)


def main():
	#---------Circle1 Class----------
	C1 = Circle1() #this is an instance of the class
	#print(type(C1))
	#print(C1)
	#print(C1.x0)
	#print(C1.y0)
	#print(C1.radius) #this applies the method to the class
	C2 = Circle2()
	#print(C2)
	#print(C2.area())
	#print(C2.implicit_equation())

	#can edit the attributes of the classes

	C3 = Circle2() #C3 is an instance of Circle2(), default class still remains intact
	C3.x0 = 3 #default class still remains intact
	C3.y0 = 7
	C3.radius = 9
	print(C3.area())
	print(C3.implicit_equation())


main()
