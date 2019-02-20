
from missile import *

class missile_creator:
    
    @staticmethod
    def create(spacecraft, speed, tam):
        x = spacecraft.x + (spacecraft.tam+2)*cos(spacecraft.direction)
        y = spacecraft.y + (spacecraft.tam+2)*sin(spacecraft.direction)
        direction = spacecraft.direction
        return missile(x, y, speed, direction, tam)
        
