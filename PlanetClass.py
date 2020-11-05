import pygame as pg
from math import sin, cos, atan2, pi
from VectorClass import Vector
import universal

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
        universal.planets.append(self)

    def plotOrbit(self):
        self.neworbitr = int(self.orbitr/universal.sf)
        if self.neworbitr >= 1:
            pg.draw.circle(universal.planetLayer, (50,50,50), (400-universal.mXoff,400-universal.mYoff), self.neworbitr, 1)

    def plot(self):
        self.newr = int(self.r/universal.sf)
        self.newx, self.newy = universal.toScreen((self.vector.x, self.vector.y))
        self.lastx, self.lasty = universal.toScreen((self.prev_vec.x, self.prev_vec.y))
        self.namel = universal.font.render(self.name, False, self.colour)
        self.labelx, self.labely = self.newx - (self.namel.get_width()/2), self.newy-self.newr-10-(self.namel.get_height()/2)
        pg.draw.circle(universal.planetLayer, self.colour, (self.newx, self.newy), self.newr)
        universal.planetLayer.blit(self.namel, (self.labelx, self.labely))
        if self.name == 'Saturn':
            pg.draw.line(universal.planetLayer, (153,76,0), (self.newx-self.newr, self.newy+self.newr), (self.newx+self.newr, self.newy-self.newr), 3)

    def plotPath(self):
        pg.draw.line(universal.pathLayer, [i/4 for i in self.colour[:-1]], (self.lastx, self.lasty), (self.newx, self.newy), 1)

    def g_refresh(self, dt):
            g=1
            r_vec = self.vector
            r_mag = r_vec.mag
            try:
                r_hat = r_vec/r_mag
            except:
                r_hat = Vector(0,0)
            try:
                f_mag = (g*self.mass*universal.sunM)/(r_mag**2)
            except:
                f_mag = 0
            f_vec = r_hat*(-f_mag)
            self.mom = self.mom + (f_vec * dt)
            self.prev_vec = self.vector
            self.vector = self.vector + ((self.mom*dt)/self.mass)
    
    def refresh(self, dt):
        self.vector.x = self.orbitr*cos(universal.t*self.v - self.off)
        self.vector.y = self.orbitr*sin(universal.t*self.v - self.off)


    def __repr__(self):
        s = f'{self.r} {self.mom} {self.vector.x} {self.vector.y} {self.colour} {self.name}'
        return s


