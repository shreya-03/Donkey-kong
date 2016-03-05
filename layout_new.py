import random
import pygame
black =(41,36,33)
#white =()
red=(176,23,31)
yellow=(238,238,0)
green=(34,139,34)
brown=(139,71,38)
orange=(255,165,0)
pygame.init()
display_width=1300
display_height=800
#gamedisplay=pygame.display.set_mode((display_width,display_height))
font=pygame.font.SysFont('comicsansms',25)
class board():
	def __init__(self):
		self.z=[[" " for i in range(60)]for j in range(27)]
#		for i in range(27):
#			self.z.append([])
#			for j in range(80):
#				self.z[i].append([])
#		print self.z
		self.boundary()
		self.gameover=False
		self.layout()
		self.player_position()
	def boundary(self):                   #creates boundary of game
		for i in range(27):
			for j in range(60):
				if i==0 or i==26:
					self.z[i][j]="X"
				else:
					if j==0 or j==59:
						self.z[i][j]="X"
					else:
						self.z[i][j]=" " 

	def layout(self):       #creates layout of game including levels,stairs and coins which are randomly created
		self.l1=random.randint(12,58)
		self.l2=random.randint(9,self.l1)
		self.l3=random.randint(self.l2,58)
		self.l4=random.randint(9,self.l3)
		self.l5=random.randint(self.l4,58)
		self.l0=random.randint(5,self.l1/2)
		for i in range(self.l0+1):
			self.z[2][i]="X"
		for i in range(self.l1+1):
			self.z[6][i]="X"
		for i in range(self.l2,60):
			self.z[10][i]="X"
		for i in range(self.l3+1):
			self.z[14][i]="X"
		for i in range(self.l4,60):
			self.z[18][i]="X"
		for i in range(self.l5+1):
			self.z[22][i]="X"
		self.z[1][2]="X"
		self.z[1][self.l0]="X"
		self.z[1][self.l0/2]="Q"
		self.h1=random.randint(3,self.l0-1)
		self.h2=random.randint(self.l2,self.l1)
		self.h3=random.randint(self.l2,self.l3)
		self.h4=random.randint(self.l4,self.l3)
		self.h5=random.randint(self.l4,self.l5)
		self.h6=random.randint(5,self.l5)
		self.h7=random.randint(self.l4,self.l3)
		for i in range(2,6):
			self.z[i][self.h1]="H"
		for i in range(6,10):
			self.z[i][self.h2]="H"
		for i in range(10,14):
			self.z[i][self.h3]="H"
		for i in range(14,18):
			self.z[i][self.h4]="H"
		for i in range(18,22):
			self.z[i][self.h5]="H"
		for i in range(22,26):
			self.z[i][self.h6]="H"
		self.z[14][self.h7]="H"
		self.z[15][self.h7]="H"
		self.z[17][self.h7]="H"
 		cnt=0
		while cnt<=20:
			x=random.randint(1,25)
		       	y=random.randint(1,59)
	 		if self.z[x+1][y]=="X" and self.z[x][y]==" ":
       				self.z[x][y]="c"
				cnt+=1 
				
	def player_position(self):      #initialise postion of player
		i=25
		j=3
		self.z[i][j]="P"
		return i,j		
	def print_layout(self):		#this function prints layout as list of list
#		for row in self.z:
#			print "".join(map(str,row))
		for i in range(27):
			for j in range(60):
				if self.z[i][j]=='X':
					print ('\033[1m'+'\033[91m'+'X'+'\033[0m'),
				elif self.z[i][j]=='H':
					print ('\033[1m'+'\033[91m'+'H'+'\033[0m'),
				elif self.z[i][j]=='c':
					print ('\033[1m'+'\033[93m'+'c'+'\033[0m'),
				elif self.z[i][j]=='P':
					print ('\033[1m'+'\033[92m'+'P'+'\033[0m'),
				elif self.z[i][j]=='D':
					print ('\033[1m'+'\033[95m'+'D'+'\033[0m'),
				elif self.z[i][j]=='Q':
					print ('\033[1m'+'\033[94m'+'Q'+'\033[0m'),
				elif self.z[i][j]=='o':
					print ('\033[1m'+'\033[96m'+'o'+'\033[0m'),
				else:
					print ('\033[1m'+'\033[96m'+' '+'\033[0m'),
			print ""
#		black=(0,0,0)
#		for i in range(27):
#			for j in range(80):
#				pygame.draw.rect(gamedisplay,black,[i,j,13,18])
#				pygame.display.set_caption('DonkeyKong')
#				if self.z[i][j]=="X":
#					text=font.render("X",True,red)
#				elif self.z[i][j]=="c":
#					text=font.render("c",True,yellow)
#				elif self.z[i][j]=="P":
#					text=font.render("P",True,green)
#				elif self.z[i][j]=="o":
#					text=font.render("o",True,orange)
#				elif self.z[i][j]=="D":
#					text=font.render("D",True,brown)
#				gamedisplay.blit(text,(i,j))
#		pygame.display.flip()
	

