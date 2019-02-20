
class missile:
    
    def __init__(self, x, y, speed, direction, tam):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.tam = tam
    
    def update_position(self, w, h):
        self.x = ( self.x + self.speed*cos(self.direction) )
        self.y = ( self.y + self.speed*sin(self.direction) )
