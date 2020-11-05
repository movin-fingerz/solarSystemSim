import pygame as pg
import PlanetClass
from PlanetClass import Planet
from VectorClass import Vector
from math import pi, degrees, atan2, sqrt
from random import randint
import universal

class Toggle:
    def __init__(self, name, val=0):
        self.name = name
        self.val = val

    def setVal(self, new):
        self.val = new

class Switch:
    def __init__(self, display, text, points, colour, fg, toggle, togVal):
        self.text = text
        self.points = points
        self.colour = colour
        self.display = display
        self.xlb = points[0]
        self.xub = self.xlb + points[2]
        self.ylb = points[1]
        self.yub = self.ylb + points[3]
        self.toggle = toggle
        self.togVal = togVal
        self.message = universal.font.render(self.text, False, fg)
        switches.append(self)
    
    def press(self):
        self.toggle.setVal(self.togVal)

    def show(self):
        if self.togVal:
            colour = mode_state_colour[self.toggle.val]
        else:
            colour = mode_state_colour[not self.toggle.val]
        pg.draw.rect(self.display, colour, self.points)
        self.display.blit(self.message, (self.points[0]+20, self.points[1]))


def definePlanets():
    global Sun
    Sun = Planet(modes[scale.val]['sizes'][0], Vector(modes[scale.val]['AUs'][0], 0), modes[scale.val]['momentum'][0], (255, 255, 0, 255), 'Sun', modes[scale.val]['AUs'][0], modes[scale.val]['mass'][0], velocities[0], 0)
    Mercury = Planet(modes[scale.val]['sizes'][1], Vector(modes[scale.val]['AUs'][1], 0), modes[scale.val]['momentum'][1], (200, 200, 200, 255), 'Mercury', modes[scale.val]['AUs'][1], modes[scale.val]['mass'][1], velocities[1], 0)
    Venus = Planet(modes[scale.val]['sizes'][2], Vector(modes[scale.val]['AUs'][2], 0),  modes[scale.val]['momentum'][2], (255, 200, 0, 255), 'Venus', modes[scale.val]['AUs'][2], modes[scale.val]['mass'][2], velocities[2], 0)
    Earth = Planet(modes[scale.val]['sizes'][3], Vector(modes[scale.val]['AUs'][3], 0),  modes[scale.val]['momentum'][3], (0, 0, 255, 255), 'Earth', modes[scale.val]['AUs'][3], modes[scale.val]['mass'][3], velocities[3], 0)
    Mars = Planet(modes[scale.val]['sizes'][4], Vector(modes[scale.val]['AUs'][4], 0),  modes[scale.val]['momentum'][4], (255, 0, 0, 255), 'Mars', modes[scale.val]['AUs'][4], modes[scale.val]['mass'][4], velocities[4], 0)
    Jupiter = Planet(modes[scale.val]['sizes'][5], Vector(modes[scale.val]['AUs'][5], 0),  modes[scale.val]['momentum'][5], (255, 87, 51, 255), 'Jupiter', modes[scale.val]['AUs'][5], modes[scale.val]['mass'][5], velocities[5], 0)
    Saturn = Planet(modes[scale.val]['sizes'][6], Vector(modes[scale.val]['AUs'][6], 0),  modes[scale.val]['momentum'][6], (255, 195, 0, 255), 'Saturn', modes[scale.val]['AUs'][6], modes[scale.val]['mass'][6], velocities[6], 0)
    Uranus = Planet(modes[scale.val]['sizes'][7], Vector(modes[scale.val]['AUs'][7], 0),  modes[scale.val]['momentum'][7], (0, 100, 255, 255), 'Uranus', modes[scale.val]['AUs'][7], modes[scale.val]['mass'][7], velocities[7], 0)
    Neptune = Planet(modes[scale.val]['sizes'][8], Vector(modes[scale.val]['AUs'][8], 0),  modes[scale.val]['momentum'][8], (0, 255, 255, 255), 'Neptune', modes[scale.val]['AUs'][8], modes[scale.val]['mass'][8], velocities[8], 0)
    Pluto = Planet(modes[scale.val]['sizes'][9], Vector(modes[scale.val]['AUs'][9], 0),  modes[scale.val]['momentum'][9], (255, 255, 255, 255), 'Pluto', modes[scale.val]['AUs'][9], modes[scale.val]['mass'][9], velocities[9], 0)

def reset():
    global t
    universal.t = 0
    universal.planets.clear()
    universal.sf = modes[scale.val]['universal.sf']
    definePlanets()
    universal.pathLayer.fill((0,0,0))
    
def zoom():
	global mlZoom
	pos = pg.mouse.get_pos()
	dx = int((pos[0] - mlZoom[0])*universal.sf)
	dy = int((pos[1] - mlZoom[1])*universal.sf)
	spPos = (pos[0] - 400 + dx, pos[1] - 400 + dy)
	universal.mXoff = int((spPos[0]/universal.sf) - spPos[0])
	universal.mYoff = int((spPos[1]/universal.sf) - spPos[1])
	mlZoom = pos
    
    
universal.planets = []
remove=[]
velocities = [0, 18, 14, 12, 10, 6, 4, 3, 2, 1]
modes={
    0:{
        'AUs': [0, 41, 55, 69, 83, 125, 172, 236, 305, 375], 
        'sizes': [30, 1, 3, 3, 2, 13, 10, 5, 5, 0], 
        'dzoom': [0.025], 
        'zoomlim': 0.1,
        'mass': [2800, 0.0042333505420753745, 0.49832214765100674, 0.5529261744966443, 0.046176262804662666, 61.23838409912236, 13.816624514305898, 1.3853460782319844, 1.3935838926174497, 0.0001274318239741738],
        'momentum': [Vector(0,0), Vector(0,0.037), Vector(0,3.6), Vector(0,3.6), Vector(0,0.28), Vector(0,300), Vector(0,60), Vector(0,5), Vector(0,4.3), Vector(0,0.00033)],
        'dt': {0: 0.005, 1: 0.9},
        'universal.sf': 1
    }, #abstract
    1:{
        'AUs': [0, 29055, 53640, 74500, 113240, 387400, 707750, 1475100, 2235000, 2942750], 
        'sizes': [350, 1, 3, 3, 2, 35, 29, 13, 13, 1], 
        'dzoom': [10,100,300, 1000], 
        'zoomlim': 1,
        'mass': [198900000, 3, 486, 597, 63, 189790, 56853, 8659, 10212, 1],
        'momentum' : [Vector(0,0), Vector(0,280), Vector(0,32000), Vector(0,32000), Vector(0,2600), Vector(0,3800000), Vector(0,900000), Vector(0,90000), Vector(0,92000), Vector(0,7)],
        'dt':  {0: 0.005, 1: 300},
        'universal.sf': 8000
    } #scalar
    }

scale = Toggle('scale')
gravity = Toggle('gravity')
linZoom = Toggle('linZoom')
play = Toggle('play', val=1)
speed = Toggle('speed', val=1)
planAdd = Toggle('planAdd')

universal.add('universal.sf', modes[scale.val]['universal.sf'])
mode_state_colour = [(255,0,0), (0,255,0)]
controlWidth=300
vMul = 1
universal.mXoff=0
universal.mYoff=0
mlZoom = (0,0)

growing=False
growtime=0
switches=[]

pg.init()

display = pg.display.set_mode((800+controlWidth,800))
universal.pathLayer.fill((0,0,0))
universal.planetLayer.fill((0,0,0,0))
clock = pg.time.Clock()
lfont = pg.font.SysFont('Arial', 18)

universal.add('sunM', modes[scale.val]['mass'][0])


definePlanets()

information = Sun
skip=False

mode_message = universal.font.render('Mode: ', False, (255,255,255))
grav_message = universal.font.render('Gravity: ', False, (255,255,255))
linZoom_message = universal.font.render('Linear Zoom: ', False, (255,255,255))
play_message = universal.font.render('Time: ', False, (255,255,255))
speed_message = universal.font.render('Speed: ', False, (255,255,255))
vel_message = universal.font.render(f'{round(vMul, 3)}', False, (255,255,255))
planAdd_message = universal.font.render('Planet Insert: ', False, (255,255,255))
planGrow_message = lfont.render('Press and hold to grow a planet.', False, (255,255,255))
planGrow2_message = lfont.render('Let go to set it off.', False, (255,255,255))
clickinfo_message = lfont.render('Click on planet / label for info.', False, (255,255,255))
name_message =   lfont.render(f'Name:     {information.name}', False, (255,255,255))
radius_message = lfont.render(f'Radius:   {information.r}', False, (255,255,255))
velocity_message =    lfont.render(f'Velocity: {information.v}', False, (255,255,255))
vec_message =    lfont.render(f'Vector:   ({round(information.vector.x,5)}, {round(information.vector.y,5)})', False, (255,255,255))
mom_message =    lfont.render(f'Momentum: {information.mom}', False, (255,255,255))
mass_message =   lfont.render(f'Mass:     {information.mass}', False, (255,255,255))
colour_message = lfont.render(f'Colour:   {information.colour}', False, (255,255,255))

abstract_button = Switch(display, ' Abstract ', (860, 40, 100, 20), mode_state_colour[not scale.val], (0,0,0), scale, 0)
scale_button = Switch(display, '    Scale', (960, 40, 100, 20), mode_state_colour[scale.val], (0,0,0), scale, 1)
gon_button = Switch(display, '     Off ', (860, 100, 100, 20), mode_state_colour[not gravity.val], (0,0,0), gravity, 0)
goff_button = Switch(display, '      On', (960, 100, 100, 20), mode_state_colour[gravity.val], (0,0,0), gravity, 1)   
linZoomOn_button = Switch(display, '     Off ', (860, 160, 100, 20), mode_state_colour[not linZoom.val], (0,0,0), linZoom, 0)
linZoomOff_button = Switch(display, '      On', (960, 160, 100, 20), mode_state_colour[linZoom.val], (0,0,0), linZoom, 1)   
play_button = Switch(display, '   Play ', (860, 220, 100, 20), mode_state_colour[play.val], (0,0,0), play, 1)
pause_button = Switch(display, '    Pause', (960, 220, 100, 20), mode_state_colour[not play.val], (0,0,0), play, 0)   
speedt_button = Switch(display, '   Up ', (860, 280, 100, 20), mode_state_colour[speed.val], (0,0,0), speed, 1)
speedf_button = Switch(display, '     Down', (960, 280, 100, 20), mode_state_colour[not speed.val], (0,0,0), speed, 0)   
planAddt_button = Switch(display, '   On ', (860, 340, 100, 20), mode_state_colour[planAdd.val], (0,0,0), planAdd, 1)
planAddf_button = Switch(display, '     Off', (960, 340, 100, 20), mode_state_colour[not planAdd.val], (0,0,0), planAdd, 0)   

print('\n:::::::::::::::::::::::::::::::::::::::::::::::\n')
universal.add('t',0)
running = True
while running:
        universal.planetLayer.fill((0,0,0,0))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse = pg.mouse.get_pos()
                    for switch in switches:
                        if (switch.xlb <= mouse[0] <= switch.xub and switch.ylb <= mouse[1] <= switch.yub):
                            switch.press()
                            if switch.toggle.name in ['scale', 'gravity']:
                                reset()
                            elif switch.toggle.name == 'speed':
                                velE_message = universal.font.render(f'{round(vMul, 3)}', False, (0,0,0))
                                display.blit(velE_message, (870, 260))
                                if switch.togVal == 1:
                                    vMul += 0.2
                                    if vMul >= 10000:
                                        vMul = 10000
                                else:
                                    vMul -= 0.2
                                    if vMul <= 0:
                                        vMul=0
                                vel_message = universal.font.render(f'{round(vMul, 3)}', False, (255,255,255))
                            break
                    if mouse[0] < 800:
                        for p in universal.planets:
                            px = p.prev_vec.x
                            py = p.prev_vec.y
                            pr = p.r
                            textrect = p.namel.get_rect()
                            textrect.x = int(px-(universal.sf*(p.namel.get_width()/2)))-(5*universal.sf)
                            textrect.y = int(py-(universal.sf*((p.namel.get_height()/2)+pr+10)))-(5*universal.sf)
                            textrect.w = (textrect.w*universal.sf) + (5*universal.sf*2)
                            textrect.h = (textrect.h*universal.sf) + (5*universal.sf*2)
                            x = (mouse[0]-400)*universal.sf
                            y = (mouse[1]-400)*universal.sf
                            sqx = (x-px)**2
                            sqy = (y-py)**2
                            print((x, y), textrect, p.name)
                            if(sqrt(sqx + sqy) < pr or textrect.collidepoint((x, y))):
                                information = p
                                skip=True
                                break
                    if(mouse[0]<=800 and not skip and planAdd.val):
                        growing=True
                    skip=False
                if event.button == 4: #zoom in
                    if not linZoom.val:
                        if not scale.val:
                            dzoom = modes[scale.val]['dzoom'][0]
                            universal.sf -= dzoom
                        else:
                            if universal.sf <= 350: dzoom = modes[scale.val]['dzoom'][0]
                            elif universal.sf <= 2000: dzoom = modes[scale.val]['dzoom'][1]
                            elif universal.sf <= 8000: dzoom = modes[scale.val]['dzoom'][2]
                            else: dzoom = modes[scale.val]['dzoom'][3]
                            universal.sf -= dzoom
                    else:
                        universal.sf -= modes[scale.val]['dzoom'][0]
                    if(universal.sf <= modes[scale.val]['zoomlim']): 
                        universal.sf=modes[scale.val]['zoomlim']
                    zoom()
                    universal.pathLayer.fill((0,0,0))
                elif event.button == 5: # zoom out
                    if not linZoom.val:
                        if not scale.val:
                            dzoom = modes[scale.val]['dzoom'][0]
                            universal.sf += dzoom
                        else:
                            if universal.sf <= 350: dzoom = modes[scale.val]['dzoom'][0]
                            elif universal.sf <= 2000: dzoom = modes[scale.val]['dzoom'][1]
                            elif universal.sf <= 8000: dzoom = modes[scale.val]['dzoom'][2]
                            else: dzoom = modes[scale.val]['dzoom'][3]
                            universal.sf += dzoom
                    else:
                        universal.sf += modes[scale.val]['dzoom'][0]
                    zoom()
                    universal.pathLayer.fill((0,0,0))
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    if growtime > 0.8:
                        coord = Vector(universal.sf*(mouse[0]-400), universal.sf*(mouse[1]-400))
                        vi = modes[scale.val]['AUs'].index(min(modes[scale.val]['AUs'], key=lambda x:abs(x-coord.mag)))
                        v = velocities[vi]
                        off = (atan2(universal.planets[vi].vector.y, universal.planets[vi].vector.x)%(2*pi)) - atan2(coord.y, coord.x)
                        new = Planet(int(growtime/2), coord, Vector(0,0.02*growtime), (randint(0,255),randint(0,255),randint(0,255),255), f'new{len(universal.planets)-9}', coord.mag, growtime*0.01, v, off)
                        growing = False
                        growtime=0
                    else:
                        growtime = 0
                        growing=False
        
        curDt = modes[scale.val]['dt'][gravity.val] * vMul

        pg.draw.rect(display, (255,255,0), (800,-1,controlWidth+1,802), 1)
        pg.draw.rect(display, (255,255,0), (800,460,controlWidth+1,340), 1)
        display.blit(mode_message, (820, 20))
        display.blit(grav_message, (820, 80))
        display.blit(linZoom_message, (820, 140))
        display.blit(play_message, (820, 200))
        display.blit(speed_message, (820, 260))
        display.blit(vel_message, (870, 260))
        display.blit(planAdd_message, (820, 320))
        display.blit(planGrow_message, (820, 380))
        display.blit(planGrow2_message, (820, 400))
        display.blit(clickinfo_message, (820, 430))

        pg.draw.rect(display, (0,0,0), (801,461,controlWidth,340))
        name_message =   lfont.render(f'Name:     {information.name}', False, (255,255,255))
        radius_message = lfont.render(f'Radius:   {information.r}', False, (255,255,255))
        velocity_message =    lfont.render(f'Velocity: {information.v}', False, (255,255,255))
        vec_message =    lfont.render(f'Vector:   ({round(information.vector.x,5)}, {round(information.vector.y,5)})', False, (255,255,255))
        mom_message =    lfont.render(f'Momentum: {information.mom}', False, (255,255,255))
        mass_message =   lfont.render(f'Mass:     {information.mass}', False, (255,255,255))
        colour_message = lfont.render(f'Colour:   {information.colour}', False, (255,255,255))

        display.blit(name_message, (820, 500))
        display.blit(radius_message, (820, 540))
        display.blit(velocity_message, (820, 580))
        display.blit(vec_message, (820, 620))
        display.blit(mom_message, (820, 660))
        display.blit(mass_message, (820, 700))
        display.blit(colour_message, (820, 740))
        
        if growing:
            growtime += 0.2
            pg.draw.circle(universal.planetLayer, (255,255,255,255), mouse, int(growtime/2))
     
        for switch in switches:
            switch.show()

        for planet in universal.planets:
            if not gravity.val:
                planet.plotOrbit()
            planet.plot()
            if play.val:
                if gravity.val:
                    planet.g_refresh(curDt)
                    planet.plotPath()
                else:
                    planet.refresh(curDt)
            if round(planet.vector.x) == 0 and round(planet.vector.y) == 0 and planet.name != 'Sun':
                remove.append(planet)
        for planet in remove:
            universal.planets.remove(planet)
            remove=[]

        if play.val:
            universal.t+=curDt
        
        pg.display.update()
        display.blit(universal.pathLayer, (0,0))
        display.blit(universal.planetLayer, (0,0))
        clock.tick(60)

pg.quit()
quit()

