
from point import *

class asteroid:
    
    def __init__(self, x0, y0, speed, direction, points):
        self.x = x0;
        self.y = y0;
        self.speed = speed;
        self.direction = direction;
        self.points = points;
    
    def update_position(self, w, h):
        self.x = ( self.x + self.speed*cos(self.direction) ) % w
        self.y = ( self.y + self.speed*sin(self.direction) ) % h
    
