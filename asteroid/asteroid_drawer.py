
from point import *

class asteroid_drawer:
    
    @staticmethod
    def draw_it(asteroid):
        
        center = point(asteroid.x, asteroid.y)
        
        xy_points = []
        for p in asteroid.points:
            l = p[0]
            a = p[1]
            
            x = l*cos(a)
            y = l*sin(a)
            
            x1 = center.x + x
            y1 = center.y + y
            
            xy_points.append(point(x1,y1))
        
        for i in range(1, len(xy_points)):
            line(xy_points[i].x, xy_points[i].y, xy_points[i-1].x, xy_points[i-1].y)
        line(xy_points[0].x, xy_points[0].y, xy_points[len(xy_points)-1].x, xy_points[len(xy_points)-1].y)
