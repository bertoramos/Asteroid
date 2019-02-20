
class spacecraft_drawer:
    
    @staticmethod
    def __get_spacecraft_corners(spacecraft):
        corners = []
        
        xp = spacecraft.x + spacecraft.tam*cos(spacecraft.direction)
        yp = spacecraft.y + spacecraft.tam*sin(spacecraft.direction)
        
        xq = spacecraft.x + spacecraft.tam*cos( ( spacecraft.direction + ((2*PI)/3) )%(2*PI) )
        yq = spacecraft.y + spacecraft.tam*sin( ( spacecraft.direction + ((2*PI)/3) )%(2*PI) )
        
        xr = spacecraft.x + spacecraft.tam*cos( ( spacecraft.direction - ((2*PI)/3) )%(2*PI) )
        yr = spacecraft.y + spacecraft.tam*sin( ( spacecraft.direction - ((2*PI)/3) )%(2*PI) )
        
        corners.append((xp,yp))
        corners.append((xq,yq))
        corners.append((xr,yr))
        
        return corners
    
    
    @staticmethod
    def draw_it(spacecraft):
        corners = spacecraft_drawer.__get_spacecraft_corners(spacecraft)
        p = corners[0]
        q = corners[1]
        r = corners[2]
        triangle(p[0], p[1], q[0], q[1], r[0], r[1])
        
        xq2 = q[0]-spacecraft.tam*cos(spacecraft.direction-(30*PI/180))
        yq2 = q[1]-spacecraft.tam*sin(spacecraft.direction-(30*PI/180))
        line(q[0],q[1],xq2,yq2)
        
        xr2 = r[0]-spacecraft.tam*cos(spacecraft.direction+(30*PI/180))
        yr2 = r[1]-spacecraft.tam*sin(spacecraft.direction+(30*PI/180))
        line(r[0],r[1],xr2,yr2)

    @staticmethod
    def draw_fire(spacecraft):
        corners = spacecraft_drawer.__get_spacecraft_corners(spacecraft)
        
        q = corners[1]
        r = corners[2]
        
        mx = (q[0] + r[0])/2.0
        my = (q[1] + r[1])/2.0
        
        m2x = mx - 10*cos(spacecraft.direction)
        m2y = my - 10*sin(spacecraft.direction)
        
        perpendicular = spacecraft.direction + (PI/2)
        
        sx = mx + 5*cos(perpendicular)
        sy = my + 5*sin(perpendicular)
        
        tx = mx + 5*cos(perpendicular - PI)
        ty = my + 5*sin(perpendicular - PI)
        
        line(sx,sy,m2x,m2y)
        line(tx,ty,m2x,m2y)
    
    
