from layout_new import *
from donkey import *
from person import *
class fireballs():
	def __init__(self,Board,d_x,d_y):
		self.x=d_x
		if d_y==Board.l1:
			self.y=d_y-1
		elif d_y<Board.l1:
		        self.y=d_y+1
		self.direction=0
		self.flag=0
	def generate_fireball(self,Board,fireball,l):
		fireball.direction=random.randint(0,1)
		Board.z[fireball.x][fireball.y]="o"
		l.append(fireball)
	def move_fireball(self,Board,l):
		i=0
		while i<len(l):
			if l[i].x==25 and l[i].y==1:
				Board.z[l[i].x][l[i].y]=" "
				del l[i]
			elif l[i].direction==0 and Board.z[l[i].x][l[i].y-1]!="X" and Board.z[l[i].x+1][l[i].y-1]!=" " and l[i].x<=25 and l[    i].y>=1 and Board.z[l[i].x+1][l[i].y]=="X":
				if  Board.z[l[i].x][l[i].y-1]!="c" and Board.z[l[i].x-2][l[i].y]==" " and l[i].flag!=1:
					Board.z[l[i].x][l[i].y-1]="o"
					Board.z[l[i].x][l[i].y]=" "
					l[i].x=l[i].x
					l[i].y=l[i].y-1
					l[i].flag=0
				elif Board.z[l[i].x-2][l[i].y]==" " and Board.z[l[i].x][l[i].y-1]=="c" and l[i].flag!=1:
					l[i].flag=1
					Board.z[l[i].x][l[i].y]=" "
					Board.z[l[i].x][l[i].y-1]="o"
					l[i].x=l[i].x
					l[i].y-=1
				elif Board.z[l[i].x-2][l[i].y]=="H" and Board.z[l[i].x][l[i].y-1]!="c" and l[i].flag!=1:
				 	Board.z[l[i].x][l[i].y]="H"
					Board.z[l[i].x][l[i].y-1]="o"
			                l[i].x=l[i].x
			                l[i].y-=1
			                l[i].flag=0
			        elif Board.z[l[i].x-2][l[i].y]=="H" and Board.z[l[i].x][l[i].y-1]=="c" and l[i].flag!=1:
			                l[i].flag=1
			                Board.z[l[i].x][l[i].y]="H"
			                Board.z[l[i].x][l[i].y-1]="o"
			                l[i].x=l[i].x
			                l[i].y-=1
			        elif l[i].flag==1 and Board.z[l[i].x][l[i].y-1]!="c":
			                Board.z[l[i].x][l[i].y]="c"
			                Board.z[l[i].x][l[i].y-1]="o"
			                l[i].x=l[i].x
			                l[i].y-=1
			                l[i].flag=0
			        elif l[i].flag==1 and Board.z[l[i].x][l[i].y-1]=="c":
			                Board.z[l[i].x][l[i].y]="c"
			                Board.z[l[i].x][l[i].y-1]="o"
			                l[i].y-=1
			                l[i].flag=1
		        elif  l[i].x<=21 and Board.z[l[i].x+3][l[i].y]==" " and l[i].direction==0 and Board.z[l[i].x+2][l[i].y]=="H":
			         Board.z[l[i].x][l[i].y-1]="o"
			         Board.z[l[i].x][l[i].y]=" "
			         l[i].x=l[i].x
			         l[i].y-=1
		        elif  l[i].x<=21 and Board.z[l[i].x+3][l[i].y]==" " and l[i].direction==1 and Board.z[l[i].x+2][l[i].y]=="H":
			         Board.z[l[i].x][l[i].y+1]="o"
			         Board.z[l[i].x][l[i].y]=" "
			         l[i].x=l[i].x
			         l[i].y=l[i].y+1
		        elif Board.z[l[i].x-1][l[i].y]==" " and Board.z[l[i].x-2][l[i].y]=="H":
			         if l[i].direction==0:
				        Board.z[l[i].x][l[i].y-1]="o"
			                Board.z[l[i].x][l[i].y]="H"
			                l[i].x=l[i].x
			                l[i].y-=1

				 if l[i].direction==1:
                                        Board.z[l[i].x][l[i].y+1]="o"
                                        Board.z[l[i].x][l[i].y]="H"
                                        l[i].x=l[i].x
                                        l[i].y+=1
                        elif Board.z[l[i].x+1][l[i].y-1]==" " and l[i].direction==0 and Board.z[l[i].x+1][l[i].y]=="X" :
	                         Board.z[l[i].x][l[i].y]=" "
	                         l[i].x+=4
                                 l[i].y-=1
                                 Board.z[l[i].x][l[i].y]="o"
                                 l[i].direction=random.randint(0,1)
	                elif Board.z[l[i].x+1][l[i].y+1]==" " and l[i].direction==1 and Board.z[l[i].x+1][l[i].y]=="X":
	                         Board.z[l[i].x][l[i].y]=" "
	                         l[i].x+=4
	                         l[i].y+=1
	                         Board.z[l[i].x][l[i].y]="o"
	                         l[i].direction=random.randint(0,1)
	                elif l[i].direction==0 and Board.z[l[i].x][l[i].y-1]=="X":
	                         l[i].direction=1
	                         Board.z[l[i].x][l[i].y+1]="o"
	                         Board.z[l[i].x][l[i].y]=" "
	                         l[i].x=l[i].x
	                         l[i].y=l[i].y+1
	                elif l[i].direction==1 and Board.z[l[i].x][l[i].y+1]!="X" and Board.z[l[i].x+1][l[i].y+1]!=" " and l[i].x<=25 and l[    i].y<=78 and Board.z[l[i].x+1][l[i].y]!="H":
	                         if Board.z[l[i].x-2][l[i].y]==" " and Board.z[l[i].x][l[i].y+1]!="c"and l[i].flag!=1:
	                                Board.z[l[i].x][l[i].y]=" "
	                                Board.z[l[i].x][l[i].y+1]="o"
	                                l[i].x=l[i].x
	                                l[i].y=l[i].y+1
	                         elif Board.z[l[i].x-2][l[i].y]==" " and Board.z[l[i].x][l[i].y+1]=="c" and l[i].flag!=1:
	                                l[i].flag=1
	                                Board.z[l[i].x][l[i].y]=" "
	                                Board.z[l[i].x][l[i].y+1]="o"
	                                l[i].x=l[i].x
	                                l[i].y+=1
				 if Board.z[l[i].x-2][l[i].y]=="H" and Board.z[l[i].x][l[i].y+1]!="c" and l[i].flag!=1:
                                        Board.z[l[i].x][l[i].y]="H"
                                        Board.z[l[i].x][l[i].y+1]="o"
                                        l[i].x=l[i].x
                                        l[i].y+=1
                                 elif Board.z[l[i].x-2][l[i].y]=="H" and Board.z[l[i].x][l[i].y+1]=="c" and l[i].flag!=1:
                                        l[i].flag=1
                                        Board.z[l[i].x][l[i].y]="H"
                                        Board.z[l[i].x][l[i].y+1]="o"
                                        l[i].x=l[i].x
                                        l[i].y+=1
                                 elif l[i].flag==1 and Board.z[l[i].x][l[i].y+1]!="c":
                                        Board.z[l[i].x][l[i].y]="c"
                                        Board.z[l[i].x][l[i].y+1]="o"
                                        l[i].x=l[i].x
                                        l[i].y+=1
                                        l[i].flag=0
                                 elif l[i].flag==1 and Board.z[l[i].x][l[i].y+1]=="c":
                                        Board.z[l[i].x][l[i].y]="c"
                                        Board.z[l[i].x][l[i].y+1]="o"
                                        l[i].y+=1
                                        l[i].flag=1
                        elif l[i].direction==1 and Board.z[l[i].x][l[i].y+1]=="X":
                                 l[i].direction=0
                                 Board.z[l[i].x][l[i].y-1]="o"
                                 Board.z[l[i].x][l[i].y]=" "
                                 l[i].x=l[i].x
   				 l[i].y=l[i].y-1
                        elif Board.z[l[i].x+1][l[i].y]=="H" and l[i].direction!=2 and Board.z[l[i].x+3][l[i].y]=="H":
                                 l[i].direction=2
                                 Board.z[l[i].x+1][l[i].y]="o"
                                 if Board.z[l[i].x-1][l[i].y]=="H":
				        Board.z[l[i].x][l[i].y]="H"
                                 elif Board.z[l[i].x-1][l[i].y]==" ":
                                        Board.z[l[i].x][l[i].y]=" "
                                 l[i].x+=1
			if l[i].direction==2 and Board.z[l[i].x+1][l[i].y]=="X":
                                 l[i].direction=random.randint(0,1)
                                 if l[i].direction==0 and Board.z[l[i].x+1][l[i].y-1]!=" ":
                                        Board.z[l[i].x][l[i].y-1]="o"
                                        Board.z[l[i].x][l[i].y]="H"
                                        l[i].x=l[i].x
                                        l[i].y-=1
                                 elif l[i].direction==0 and Board.z[l[i].x+1][l[i].y-1]==" ":
                                        Board.z[l[i].x][l[i].y]="H"
                                        l[i].x+=4
                                        l[i].y-=1
                                        Board.z[l[i].x][l[i].y]="o"
                                        l[i].direction=random.randint(0,1)
                                 elif l[i].direction==1 and Board.z[l[i].x+1][l[i].y+1]!=" ":
                                        Board.z[l[i].x][l[i].y+1]="o"
                                        Board.z[l[i].x][l[i].y]="H"
                                        l[i].x=l[i].x
                                        l[i].y+=1
                                 elif l[i].direction==1 and Board.z[l[i].x+1][l[i].y+1]==" ":
                                        Board.z[l[i].x][l[i].y]="H"
                                        l[i].x+=4
                                        l[i].y+=1
                                        Board.z[l[i].x][l[i].y]="o"
                                        l[i].direction=random.randint(0,1)
                        elif l[i].direction==2 and Board.z[l[i].x+1][l[i].y]=="H":
                                 if Board.z[l[i].x+1][l[i].y-1]=="X" or Board.z[l[i].x+1][l[i].y+1]=="X":
                                        if Board.z[l[i].x+3][l[i].y]==" " and Board.z[l[i].x+2][l[i].y]=="H":
                                                l[i].direction=random.randint(0,1)
                                                if l[i].direction==1:
                                                        Board.z[l[i].x][l[i].y+1]="o"
                                                        Board.z[l[i].x][l[i].y]="H"
                                                        l[i].x=l[i].x
                                                        l[i].y+=1
                                                else:
                                                        Board.z[l[i].x][l[i].y-1]="o"
							ard.z[l[i].x][l[i].y]="H"
                                                        l[i].y-=1
                                        elif Board.z[l[i].x+3][l[i].y]=="H":
                                                l[i].direction=2
                                                Board.z[l[i].x+1][l[i].y]="o"
                                                Board.z[l[i].x][l[i].y]="H"
                                                l[i].x+=1
                                 else:
                                        l[i].direction=2
                                        Board.z[l[i].x+1][l[i].y]="o"
                                        Board.z[l[i].x][l[i].y]="H"
                                        l[i].x+=1
                        elif l[i].direction==2 and Board.z[l[i].x+1][l[i].y]==" ":
                                 Board.z[l[i].x][l[i].y]="H"
                                 l[i].x+=4
                                 l[i].y=self.y
                                 Board.z[l[i].x][l[i].y]="o"
                                 l[i].direction=random.randint(0,1)
                                 if l[i].direction==1:
                                        if Board.z[l[i].x][l[i].y+1]!="X":
                                                Board.z[l[i].x][l[i].y+1]="o"
                                                Board.z[l[i].x][l[i].y]=" "
                                                l[i].y+=1
                                        else:
                                                Board.z[l[i].x][l[i].y-1]="o"
                                                Board.z[l[i].x][l[i].y]=" "
                                                l[i].y-=1
                                                l[i].direction=0
                                 elif l[i].direction==0:
                                        if Board.z[l[i].x][l[i].y-1]!="X":
                                                Board.z[l[i].x][l[i].y-1]="o"
                                                Board.z[l[i].x][l[i].y]=" "
                                                l[i].y-=1
                                        else:
                                                Board.z[l[i].x][l[i].y+1]="o"
                                                Board.z[l[i].x][l[i].y]=" "

                                                l[i].y+=1
                                                l[i].direction=1
                        elif l[i].direction==2 and Board.z[l[i].x+1][l[i].y]==" ":
                                 Board.z[l[i].x][l[i].y]=" "
                                 l[i].x+=4
                                 l[i].y=l[i].y
                                 Board.z[l[i].x][l[i].y]="o"
                                 l[i].direction=random.randint(0,1)
                        elif l[i].direction==2 and Board.z[l[i].x+1][l[i].y]=="P":
                                 Board.z[l[i].x][l[i].y]="H"
                                 Board.z[l[i].x+1][l[i].y]="o"
                                 l[i].x+=1
                                 l[i].direction=random.randint(0,1)
                        i+=1
	def checkcollision(self,l,Board,p):
                i=0
                while i<len(l):
                        if p.x==l[i].x and p.y==l[i].y-1 and l[i].direction==0:
                                 if p.life>=1:
                                 	p.x=25
                                 	p.y=1
                                        Board.z[p.x][p.y]="P"
                                        Board.z[l[i].x][l[i].y-1]=" "
                                        p.life-=1
                                        p.score-=25
#                                       player_score-=25
                                 else:
                                        Board.gameover=True
                                 break
                        elif p.x==l[i].x and p.y==l[i].y+1 and l[i].direction==1:
                                 if p.life>=1:
                                        p.x=25
                                        p.y=1
                                        Board.z[p.x][p.y]="P"
                                        Board.z[l[i].x][l[i].y+1]=" "
                                        p.life-=1
					p.score-=25
#                                       player_score-=25
                                 else:
                                        Board.gameover=True
                                 break
                        elif p.x==l[i].x+1 and p.y==l[i].y and l[i].direction==2:
                                 if p.life>=1:
                                        p.x=25
                                        p.y=1
                                        Board.z[p.x][p.y]="P"
                                        Board.z[l[i].x+1][l[i].y]="H"
                                        p.life-=1
                                        p.score-=25
#                                       player_score-=25
                                 else:
                                        Board.gameover=True
                                 break
                        i+=1

