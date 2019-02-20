
from missile import *
from missile_creator import *

class spacecraft:
    def __init__(self, x0, y0, turning_speed, direction, tam):
        self.x = x0
        self.y = y0
        self.speed = 0 # pixeles por instante
        self.turning_speed = turning_speed
        self.direction = direction # radianes
        self.tam = tam

    def turn_left(self):
        dir = self.direction - self.turning_speed*((2*PI)/360.0)
        self.direction = dir%(2*PI)
        
    def turn_right(self):
        dir = self.direction + self.turning_speed*((2*PI)/360.0)
        self.direction = dir%(2*PI)
    
    def speed_up(self):
        self.speed = self.speed + 1;
        
    def brake(self):
        self.speed = self.speed - 1;

    def update_position(self, w, h):
        self.x = ( self.x + self.speed*cos(self.direction) ) % w
        self.y = ( self.y + self.speed*sin(self.direction) ) % h
    
    def shoot(self):
        return missile_creator.create(self, 10, 2)
