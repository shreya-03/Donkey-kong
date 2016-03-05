from layout_new import *
from person import *
#from donkey import *
class donkey(person):   #donkey class is inherited from person class
	def __init__(self,Board):  #this is called when object is created and declares class data member and also initialises them
		x=5
		y=2
		self.flag=0
		person.__init__(self,x,y)
		Board.z[x][y]="D"
	def random_position(self,Board):  #this function makes position of donkey random 
		if Board.z[self.x-1][self.y]=="H":
			Board.z[self.x][self.y]="H"
		elif self.flag==1:
			Board.z[self.x][self.y]="c"
			self.flag=0
		elif Board.z[self.x-1][self.y]==" ":
			Board.z[self.x][self.y]=" "
		self.y=random.randint(4,Board.l1)
		self.x=5
		if Board.z[self.x][self.y]=="c":
			self.flag=1
		Board.z[self.x][self.y]="D"

