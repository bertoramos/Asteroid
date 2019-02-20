
from asteroid import *
from random import *

class asteroid_creator:
    
    @staticmethod
    def sort_points(points):
        for i in range(1, len(points)):
            k = points[i]
            j = i - 1
            while j >= 0 and k[1] < points[j][1]:
                points[j + 1] = points[j]
                j -= 1
            points[j + 1] = k
    
    
    @staticmethod
    def create(sides, radix, x0, y0, speed0, direction0):
        points = []
        for i in range(sides):
            l = uniform(radix/2.0,radix)
            a = uniform(0,2*PI)
            points.append((l, a));
        
        asteroid_creator.sort_points(points)
        
        return asteroid(x0, y0, speed0, direction0, points)
    
