from layout_new import *
import time 
import random
import pygame
import os
from donkey import *
from person import *
from fireball import *
#from threading import Thread
# getchar() function returns a single character from standard input and is taken from Github : https://gist.github.com/jasonrdsouza/1901709
def getchar():                    
	import tty,termios,sys
	fd=sys.stdin.fileno()
	old_settings=termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch=sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd,termios.TCSADRAIN,old_settings)
	return ch
class player(person):  #class player is inherited from person class
	def __init__(self,x_coordinate,y_coordinate,Board):   # this is called when object is created and declares class data member and initialises them
		person.__init__(self,x_coordinate,y_coordinate)
		self.score=0
#		global player_score
		self.life=3
		self.move=""
	def getposition(self,Board):   #this function takes character as input and then decides movement according to character given as input but for left jump press space+'a' and for right jump press space+'d' and for simple jump press space+space and also checks collision of player with fireball
		self.move=getchar()
		if self.move=="q":   #use to exit the game
			exit()
		elif self.move=="a": #enter a for left movement
			if self.checkwall(self.x,self.y-1,Board)==1:
				if Board.z[self.x][self.y-1]=="o":
					if self.life>=1:
						self.x=25
						self.y=1
						Board.z[self.x][self.y]="P"
						self.life-=1
						self.score-=25
#						player_score-=25
					else:
						Board.gameover=True
				elif Board.z[self.x+1][self.y-1]==" " and  Board.z[self.x-2][self.y]!="H":
					Board.z[self.x][self.y]=" "
					self.x+=4
					self.y=self.y-1
					Board.z[self.x][self.y]="P"
				elif Board.z[self.x+1][self.y-1]==" " and Board.z[self.x-2][self.y]=="H":
					Board.z[self.x][self.y]="H"
					self.x+=4
					self.y+=1
					Board.z[self.x][self.y]="P"
				elif Board.z[self.x-2][self.y]=="H" and Board.z[self.x+1][self.y-1]!=" ":
					Board.z[self.x][self.y-1]="P"
					Board.z[self.x][self.y]="H"
					self.x=self.x
					self.y=self.y-1
				else:
					Board.z[self.x][self.y-1]="P"
					Board.z[self.x][self.y]=" "
					self.x=self.x
					self.y=self.y-1
		elif self.move=="d":   # enter d for right movement
			if self.checkwall(self.x,self.y+1,Board)==1:
				if Board.z[self.x][self.y+1]=="o":
					if self.life>=1:
						self.x=25
						self.y=1
						Board.z[self.x][self.y]="P"
						self.life-=1
						self.score-=25
#						player_score-=25
					else:
						Board.gameover=True
				elif Board.z[self.x+1][self.y+1]==" " and Board.z[self.x-1][self.y]!="H":
					Board.z[self.x][self.y]=" "
					self.x+=4
					self.y+=1
					Board.z[self.x][self.y]="P"
				elif Board.z[self.x+1][self.y+1]==" " and Board.z[self.x-1][self.y]=="H":
					Board.z[self.x][self.y]="H"
					self.x+=4
					self.y+=1
					Board.z[self.x][self.y]="P"
				elif Board.z[self.x-2][self.y]=="H":
					Board.z[self.x][self.y+1]="P"
					Board.z[self.x][self.y]="H"
					self.x=self.x
					self.y=self.y+1
				else:
					Board.z[self.x][self.y+1]="P"
					Board.z[self.x][self.y]=" "
					self.x=self.x
					self.y=self.y+1
		elif self.move=="w":	#enter w to climb unbroken stairs only
			if self.checkwall(self.x-1,self.y,Board)==1:
				if Board.z[self.x-1][self.y]=="o":
					if self.life>=1:
						Board.z[self.x][self.y]="H"
						self.x=25
						self.y=1
						Board.z[self.x][self.y]="P"
						self.life-=1
						self.score-=25
					else:
						Board.gameover=True
				elif Board.z[self.x-1][self.y]!="H" and (Board.z[self.x][self.y-1]!="X" and Board.z[self.x][self.y+1]!="X"):
					self.x=self.x
					self.y=self.y
				elif Board.z[self.x-1][self.y]=="H" or (Board.z[self.x][self.y-1]=="X"or Board.z[self.x][self.y+1]=="X"):
					Board.z[self.x-1][self.y]="P"
					Board.z[self.x][self.y]="H"
					self.x=self.x-1
					
		elif self.move=="s":     #enter s to come down from stairs
			if self.checkwall(self.x+1,self.y,Board)==1:
				if Board.z[self.x+1][self.y]=="o":
					if self.life>=1:
						Board.z[self.x][self.y]="H"
						self.x=25
						self.y=1
						Board.z[self.x][self.y]="P"
						self.life-=1
						self.score-=25
					else:
						Board.gameover=True
				elif Board.z[self.x+1][self.y]=="H":
					if Board.z[self.x+1][self.y-1]=="X" or Board.z[self.x+1][self.y+1]=="X":
						Board.z[self.x+1][self.y]="P"
						Board.z[self.x][self.y]=" "
						self.x+=1
					elif Board.z[self.x+1][self.y-1]==" " or Board.z[self.x+1][self.y+1]==" ":
						Board.z[self.x+1][self.y]="P"
						Board.z[self.x][self.y]="H"
						self.x+=1
		elif self.move==" ":    # enter space for jump
			self.move=getchar()
			if self.move=="w":
                        	if Board.z[self.x-1][self.y]!="H":
                              		Board.z[self.x-1][self.y]="P"
                                  	Board.z[self.x][self.y]=" "
                                  	self.x-=1
                                  	Board.print_layout()
                                        time.sleep(0.2)
                                  	if Board.z[self.x-1][self.y]!="H":
                                      	        Board.z[self.x-1][self.y]="P"
                                                Board.z[self.x][self.y]=" "
                                                self.x-=1
                                                Board.print_layout()
                                                time.sleep(0.2)
                                                Board.z[self.x+1][self.y]="P"
                                                Board.z[self.x][self.y]=" "
                                          	self.x+=1
                                          	Board.print_layout()
                                                time.sleep(0.2)
                                          	Board.z[self.x+1][self.y]="P"
                                          	Board.z[self.x][self.y]=" "
                                          	self.x+=1
                                          	Board.print_layout()
													

			elif self.move=="a":       
				if Board.z[self.x-1][self.y-1]!="H" or Board.z[self.x-1][self.y-1]!="X":
					Board.z[self.x-1][self.y-1]="P"
					Board.z[self.x][self.y]=" "
					self.x-=1
					self.y-=1
					Board.print_layout()
					time.sleep(0.2)
					if Board.z[self.x-1][self.y-1]!="H" or Board.z[self.x-1][self.y-1]!="X":
						Board.z[self.x-1][self.y-1]="P"
						Board.z[self.x][self.y]=" "
						self.x-=1
						self.y-=1
						Board.print_layout()
						time.sleep(0.2)
						if Board.z[self.x+1][self.y-1]!="H" or Board.z[self.x+1][self.y-1]!="X":
							Board.z[self.x+1][self.y-1]="P"
							Board.z[self.x][self.y]=" "
							self.x+=1
							self.y-=1
							Board.print_layout()
							time.sleep(0.2)
							if Board.z[self.x+1][self.y-1]!="H" or Board.z[self.x+1][self.y-1]!="X":
								Board.z[self.x+1][self.y-1]="P"
								Board.z[self.x][self.y]=" "
								self.x+=1
								self.y-=1
								Board.print_layout()
							elif Board.z[self.x+1][self.y-1]=="H" or Board.z[self.x+1][self.y-1]=="X":
								Board.z[self.x+1][self.y]="P"
								Board.z[self.x][self.y]=" "
								self.x+=1
								self.y=self.y
								Board.print_layout()
							elif Board.z[self.x+1][self.y-1]=="o":
								if self.life>=1:
									Board.z[self.x][self.y]=" "
									self.x=25
									self.y=1
									Board.z[self.x][self.y]="P"
									self.life-=1
									self.score-=25
									Board.print_layout()
								elif self.life==0:
									Board.gameover=True
						elif Board.z[self.x+1][self.y-1]=="H" or Board.z[self.x+1][self.y-1]=="X":
							Board.z[self.x+2][self.y]="P"
							Board.z[self.x][self.y]=" "
							self.x+=2
							self.y+=1
							Board.print_layout()
							time.sleep(0.2)
					elif Board.z[self.x-1][self.y-1]=="H" or Board.z[self.x-1][self.y-1]=="X":
						Board.z[self.x+1][self.y]="P"
						Board.z[self.x][self.y]=" "
						self.x+=1
						Board.print_layout()
					
			elif self.move=="d":    # d here denote for right jump
		     		if Board.z[self.x-1][self.y+1]!="H" or Board.z[self.x-1][self.y+1]!="X":
					Board.z[self.x-1][self.y+1]="P"
	   				Board.z[self.x][self.y]=" "
		 			self.x=self.x-1
		  			self.y+=1
					Board.print_layout()
					time.sleep(0.2)
					if Board.z[self.x-1][self.y+1]!="H" or Board.z[self.x-1][self.y+1]!="X":	
						Board.z[self.x-1][self.y+1]="P"
						Board.z[self.x][self.y]=" "
						self.x-=1
						self.y+=1
						Board.print_layout()
						time.sleep(0.2)
						if Board.z[self.x+1][self.y+1]!="H" or Board.z[self.x+1][self.y+1]!="X":	
							Board.z[self.x+1][self.y+1]="P"
							Board.z[self.x][self.y]=" "
							self.x+=1
							self.y+=1
							Board.print_layout()
							time.sleep(0.2)
							if Board.z[self.x+1][self.y+1]!="H" or Board.z[self.x+1][self.y+1]!="X":
								Board.z[self.x+1][self.y+1]="P"
								Board.z[self.x][self.y]=" "
								self.x+=1
								self.y+=1
								Board.print_layout()
							elif Board.z[self.x+1][self.y+1]=="H" or Board.z[self.x+1][self.y+1]=="X":
								Board.z[self.x+1][self.y]="P"
								Board.z[self.x][self.y]=" "
								self.x+=1
								Board.print_layout()
							elif Board.z[self.x+1][self.y+1]=="o":
								if self.life>=1:
									Board.z[self.x][self.y]=" "
									self.x=25
									self.y=1
									Board.z[self.x][self.y]="P"
									self.life-=1
									self.score-=25
									Board.print_layout()
								else:
									Board.gameover=True
						elif Board.z[self.x+1][self.y+1]=="H" or Board.z[self.x+1][self.y+1]=="X":
							Board.z[self.x+2][self.y]="P"
							Board.z[self.x][self.y]=" "
							self.x+=2
							Board.print_layout()
							time.sleep(0.2)
					elif Board.z[self.x-1][self.y+1]=="H" or Board.z[self.x-1][self.y+1]=="X":
						Board.z[self.x+1][self.y]="P"
						Board.z[self.x][self.y]=" "
						self.x+=1
						Board.print_layout()
						time.sleep(0.2)	
	def scoreofplayer(self):   #since score is private member to fetch score this function is for encapsulation
		return self.score
	def checkcoin(self,Board):  #this function check coin during player movement
		if Board.z[self.x][self.y+1]=="c" and self.move=="d":
			return True
		elif Board.z[self.x][self.y-1]=="c" and self.move=="a":
			return True
		elif Board.z[self.x-1][self.y]=="c" and self.move=="w":
			return True
		return False
	def coins_collected(self,Board):  #increment score value when player encountered coin on his way
		self.score+=5
#		print  self.score
#		player_score+=5
		Board.z[self.x][self.y]=" "
	def checkcollision(self,Board,d): #this function checks collision of player with donkey and decrement player life and if zero game is over
		if self.x==d.x and self.y==d.y:
			if self.life>0:
				self.x=25
				self.y=1
				Board.z[self.x][self.y]="p"
				self.life-=1
				self.score-=25
			else:
				Board.gameover=True
		
def main():
	level=3
	current_level=1
	pygame.init()
#	display_width=800
#	display_height=600
#	gamedisplay=pygame.display.set_mode((display_width,display_height))
#	pygame.display.set_caption('Donkeykong')
	Board=board()
	while current_level<=level :
#		Board=board()
		Board.gameover=False
		Board.boundary()
		Board.layout()
		Board.player_position()
		playercoordinates=Board.player_position()
		p=player(playercoordinates[0],playercoordinates[1],Board)
		d=donkey(Board)
		Board.print_layout()
		cnt=0
		player_score=0
		l=[]
		while Board.gameover==False:
			p.getposition(Board)
			d.random_position(Board)
			p.checkcollision(Board,d)
			if Board.gameover==False:
				if cnt%(20*(4-current_level))==0:
					fireball=fireballs(Board,d.x,d.y)
					fireball.generate_fireball(Board,fireball,l)
#fireball.move_fireball(Board,l)
				fireball.checkcollision(l,Board,p)
				fireball.move_fireball(Board,l)
				if p.checkcoin(Board)==True:
					p.coins_collected(Board)
					player_score=p.scoreofplayer()
				os.system('clear')
				Board.print_layout()
				print "score: "+str(p.score)
				print "level :"+str(current_level)
#				os.system('clear')
				cnt+=1
			if p.x==1 and p.y==Board.l0/2:
		       		os.system('clear')
				#Board.gameover=True
				Board.print_layout()
#				Board.gameover=True
				print "congratulations reached next level with score:"+str(p.score)
				break
#				os.system('clear')	
			elif Board.gameover==True:
				os.system('clear')
				Board.print_layout()
				print "Game over and your score was" +str(p.score)
#				os.system('clear')
		if Board.gameover==True:
			break
		else:
			current_level+=1		
main()
