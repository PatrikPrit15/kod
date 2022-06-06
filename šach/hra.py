import itertools
import tkinter as tk



main = tk.Tk()
canvas = tk.Canvas(width=1920, height=1080)
canvas.pack()
import time



# nic-0, pesiakb-1, konb-2, strelecb-3, vezab-4, kralovnab-5, kralb-6,pesiakc-7, konc-8, strelecc-9, vezac-10, kralovnac-11, kralc-12
pole = [
	[[10,0],[8,0],[9,0],[11,0],[12,0],[9,0],[8,0],[10,0]],
	[[7,0] for _ in range(8)],
	[[0,0] for _ in range(8)],
	[[0,0] for _ in range(8)],
	[[0,0] for _ in range(8)],
	[[0,0] for _ in range(8)],
	[[1,0] for _ in range(8)],
	[[4,0],[2,0],[3,0],[5,0],[6,0],[3,0],[2,0],[4,0]]
]




sur=[-1,-1]
empasant=[-1,-1]
rbl,rbp,rcl,rcp=0,0,0,0

def create_board():
	farba = 1
	for y in range(8):
		farba = not farba
		for x in range(8):
			canvas.create_rectangle(
				50 + x * 90,
				50 + y * 90,
				140 + x * 90,
				140 + y * 90,
				fill="#573a2e" if farba else "#fccc74",
			)
			farba = not farba
			time.sleep(0.0005)
			canvas.update()
	time.sleep(0.3)

def init_board():
	global pole
	for y, x in itertools.product(range(8), range(8)):
		if pole[y][x][0]>0:
			pole[y][x][1]=canvas.create_image(95+90*x, 95+90*y, image=images[pole[y][x][0]-1])
			#time.sleep(0.1)
	canvas.update()

def loadimages():
	return [tk.PhotoImage(file=f'{i}.png') for i in range(1,13)]

def update_board():
	for a, b in itertools.product(range(8), range(8)):#=2 loopy
		canvas.delete(pole[a][b][1])
	init_board()

def klik(event):  
	global sur
	if 0<=(event.y-50)//90<=7 and 0<=(event.x-50)//90<=7:
		sur[0]=(event.x-50)//90
		sur[1]=(event.y-50)//90

def drag(event):
	if 0<=(event.y-50)//90<=7 and 0<=(event.x-50)//90<=7:
		canvas.coords(pole[sur[1]][sur[0]][1], event.x, event.y)

def release(event):
	global pole,sur
	if (0 <= (event.y - 50) // 90 <= 7
	and 0 <= (event.x - 50) // 90 <= 7
	and pole[sur[1]][sur[0]][0] != 0
	and validator((event.y - 50) // 90, (event.x - 50) // 90)):
		pole[(event.y-50)//90][(event.x-50)//90][0]=pole[sur[1]][sur[0]][0]
		if (event.y-50)//90!=sur[1] or (event.x-50)//90!=sur[0]:
			pole[sur[1]][sur[0]][0]=0
	update_board()

def validator(y,x):
	global rbl,rbp,rcl,rcp,pole,empasant
	if pole[7][4][0]!=6:rbl,rbp=0,0
	if pole[7][0][0]!=4:rbl=0
	if pole[7][7][0]!=4:rbp=0
	if pole[0][4][0]!=12:rcl,rcp=0,0
	if pole[0][0][0]!=10:rcl=0
	if pole[0][7][0]!=10:rcp=0
	if 0<pole[sur[1]][sur[0]][0]<7 and 0<pole[y][x][0]<7 or pole[sur[1]][sur[0]][0]>6 and pole[y][x][0]>6: #nie su rovnaka farba
		return 0

	if pole[sur[1]][sur[0]][0]==1:#biely pesiak
		if sur[1]-y<=0:
			return 0
		if sur[0]==x:
			if pole[y][x][0]!=0 or pole[max(0,sur[1]-1)][sur[0]][0]!=0:
				return 0
			if sur[1]-y>1 and sur[1]!=6:
				return 0
			if sur[1]-y>2:
				return 0
			if sur[1]-y==2:
				empasant=[x,y+1]
				return 1
		elif sur[1]-y>1:
			return 0
		elif abs(sur[0]-x)>1:
			return 0
		if sur[0]!=x and (pole[y][x][0]==0 and (y!=empasant[1] and x!=empasant[0])):
			return 0
		if (y==empasant[1] and x==empasant[0]):
			pole[empasant[1]+1][empasant[0]][0]=0
		if y==0:
			pole[sur[1]][sur[0]][0]=5

	if pole[sur[1]][sur[0]][0]==7:#cierny pesiak
		if y-sur[1]<=0:
			return 0
		if sur[0]==x:
			if pole[y][x][0]!=0 or pole[min(7,sur[1]+1)][sur[0]][0]!=0:
				return 0
			if y-sur[1]>1 and sur[1]!=1:
				return 0
			if y-sur[1]>2:
				return 0
			if y-sur[1]==2:
				empasant=[x,y-1]
				return 1
		elif y-sur[1]>1:
			return 0
		elif abs(sur[0]-x)>1:
			return 0
		if sur[0]!=x and (pole[y][x][0]==0 and y!=empasant[1] and x!=empasant[0]):
			return 0
		if (y==empasant[1] and x==empasant[0]):
			pole[empasant[1]-1][empasant[0]][0]=0
		if y == 7:
			pole[sur[1]][sur[0]][0] = 11


	empasant=[-1,-1]
	if pole[sur[1]][sur[0]][0] in [2, 8]: #kon
		if abs(x - sur[0]) != 1 or abs(y - sur[1]) != 2:
			if abs(x - sur[0]) != 2 or abs(y - sur[1]) != 1: 
				return 0

	if pole[sur[1]][sur[0]][0] in [3,9]:#strelec
		if abs(x-sur[0])!=abs(y-sur[1]):
			return 0
		h,v=1 if x-sur[0]>0 else -1,1 if y-sur[1]>0 else -1
		for i in range(1,10):
			if sur[0]+h*i==x and sur[1]+v*i==y:
				break
			if pole[sur[1]+v*i][sur[0]+h*i][0]!=0:
				return 0

	if pole[sur[1]][sur[0]][0] in [4,10]:#veza
		if x==sur[0] and y!=sur[1]:
			if any(pole[i][x][0]!=0 for i in range(min(y, sur[1]) + 1, max(y, sur[1]))):
				return 0
		elif x!=sur[0] and y==sur[1]:
			if any(pole[y][i][0]!=0 for i in range(min(x, sur[0]) + 1, max(x, sur[0]))):
				return 0
		else:
			return 0

	if pole[sur[1]][sur[0]][0] in [5,11]:#kralovna
		if abs(x - sur[0]) == abs(y - sur[1]):#je strelec
			h,v=1 if x-sur[0]>0 else -1, 1 if y-sur[1]>0 else -1 
			for i in range(1,10):
				if sur[0]+h*i==x and sur[1]+v*i==y:
					break
				if pole[sur[1]+v*i][sur[0]+h*i][0]!=0:
					return 0

		elif x==sur[0] and y!=sur[1]: #je veza
			if any(pole[i][x][0] != 0 for i in range(min(y, sur[1]) + 1, max(y, sur[1]))):
				return 0
		elif x!=sur[0] and y==sur[1]:
			if any(pole[y][i][0] != 0 for i in range(min(x, sur[0]) + 1, max(x, sur[0]))):
				return 0
		else:
			return 0

	if pole[sur[1]][sur[0]][0]==6:#kralb
		if abs(y-sur[1])>1 or abs(x-sur[0])>1:
			if y-sur[1]!=0:
				return 0
			if rbl==0 and rbp==0:
				return 0
			if abs(x-sur[0])!=2:
				return 0
			if x>sur[0]:
				if not rbp or any([pole[7][i][0]!=0 for i in range(5,7)]):
					return 0
				pole[7][7][0]=0
				pole[7][5][0]=4
			else:
				if not rbl or any([pole[7][i][0]!=0 for i in range(1,4)]):
					return 0
				pole[7][0][0]=0
				pole[7][3][0]=4

	if pole[sur[1]][sur[0]][0]==12:#kralc
		if abs(y-sur[1])>1 or abs(x-sur[0])>1:
			if y-sur[1]!=0:
				return 0
			if rcl==0 and rcp==0:
				return 0
			if abs(x-sur[0])!=2:
				return 0
			if x>sur[0]:
				if not rcp or any([pole[0][i][0]!=0 for i in range(5,7)]):
					return 0
				pole[0][7][0]=0
				pole[0][5][0]=10
			else:
				if not rcl or any([pole[0][i][0]!=0 for i in range(1,4)]):
					return 0
				pole[0][0][0]=0
				pole[0][3][0]=10

	return 1

#run
create_board()
images=loadimages()
init_board()
canvas.bind("<Button-1>", klik)
canvas.bind("<B1-Motion>", drag)
canvas.bind("<ButtonRelease-1>", release)
canvas.mainloop()