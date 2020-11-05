import pygame as pg

def toScreen(coord):
	x = coord[0]
	y = coord[1]
	
	newx = int(x/sf) + 400 - mXoff
	newy = int(y/sf) + 400 - mYoff
	
	return (newx, newy)
	
def toSpace(coord):
	x = coord[0]
	y = coord[1]
	
	newx = int((x-400+mXoff)*sf)
	newy = int((y-400+mYoff)*sf)
	
	return (newx, newy)

def add(name, value):
	globals()[name] = value
	
pg.font.init()
	
planetLayer = pg.Surface((800,800), pg.SRCALPHA)
font = pg.font.SysFont('Arial', 16)
planets=[]
pathLayer = pg.Surface((800,800))
mXoff=0
mYoff=0
sf=1
t=0
	
