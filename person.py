from layout_new import *
class person():
	def __init__(self,x_coordinate,y_coordinate): #this is called automatically when object is created and initialises coordinate with passed value as argument
		self.x=x_coordinate
		self.y=y_coordinate
	def getposition(self): #this function has no body
		pass
	def checkwall(self,x_coordinate,y_coordinate,Board): #this function checks wall if there there is wall at particular coordinate if ther is wall present return 0 else return 1
		if Board.z[x_coordinate][y_coordinate]!="X":
			return 1
		if x_coordinate>=26 or x_coordinate<=0:
			return 0
		if y_coordinate<=0 or y_coordinate>=59:
			return 0
		return 1

