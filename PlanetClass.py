import pygame as pg
from math import sin, cos, atan2, pi
from VectorClass import Vector

class Planet:
    def __init__(self, r, vector, mom, colour, name, orbitr, mass, v, off):
        self.r = r
        self.vector = vector
        self.mom = mom
        self.colour = colour
        self.name = name
        self.orbitr = orbitr
        self.mass = mass
        self.prev_vec = self.vector
        self.v = v
        self.off = off
        self.theta = (atan2(self.vector.y, self.vector.x)%(2*pi))
        planets.append(self)

    def plotOrbit(self, sf):
        self.newr = int(self.r/sf)
        self.neworbitr = int(self.orbitr/sf)
        if self.neworbitr >= 1:
            pg.draw.circle(display, (50,50,50), (400,400), self.neworbitr, 1)

    def plot(self, sf):
        self.newx = int(self.vector.x/sf)#+700
        self.newy = int(self.vector.y/sf)#+400
        self.lastx = int(self.prev_vec.x/sf)
        self.lasty = int(self.prev_vec.y/sf)
        self.newr = int(self.r/sf)
        pg.draw.circle(display, self.colour, (self.newx+400, self.newy+400), self.newr)
        self.namel = font.render(self.name, False, self.colour)
        display.blit(self.namel, (self.newx-(self.namel.get_width()/2)+400, self.newy-(self.namel.get_height()/2)+390-self.newr))
        if self.name == 'Saturn':
            pg.draw.line(display, (153,76,0), (self.newx+400-self.newr, self.newy+400+self.newr), (self.newx+400+self.newr, self.newy+400-self.newr), 3)

    def plotPath(self):
        pg.draw.line(pathL, [i/4 for i in self.colour[:-1]], (self.lastx+400, self.lasty+400), (self.newx+400, self.newy+400), 1)

    def g_refresh(self, t, dt):
            g=1
            r_vec = self.vector
            r_mag = r_vec.mag
            try:
                r_hat = r_vec/r_mag
            except:
                r_hat = Vector(0,0)
            try:
                f_mag = (g*self.mass*sunM)/(r_mag**2)
            except:
                f_mag = 0
            f_vec = r_hat*(-f_mag)
            self.mom = self.mom + (f_vec * dt)
            self.prev_vec = self.vector
            self.vector = self.vector + ((self.mom*dt)/self.mass)
    
    def refresh(self, t, dt):
        self.vector.x = self.orbitr*cos(t*self.v - self.off)
        self.vector.y = self.orbitr*sin(t*self.v - self.off)


    def __repr__(self):
        s = f'{self.r} {self.mom} {self.vector.x} {self.vector.y} {self.colour} {self.name}'
        return s

def init(displayy, fontt, planetss, sunMM, pathLL):
    global display, font, planets, sunM, pathL
    display = displayy
    font = fontt
    planets = planetss
    sunM = sunMM
    pathL = pathLL
