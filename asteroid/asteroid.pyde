
from random import *

from asteroid_creator import *
from asteroid_drawer import *
from asteroid import *
from spacecraft import spacecraft
from spacecraft_drawer import *
from missile import *
from missile_creator import *
from missile_drawer import *

sc = spacecraft(250,250,5,-(PI/2),15)
asteroids = []
num_asteroids = 10
tam = 15

missiles = []

def setup():
    size(500,500)
    for i in range(num_asteroids):
        x0 = randint(0,500)
        y0 = randint(0,500)
        speed = uniform(1,2)
        sides = randint(5,15)
        radix = uniform(25,50)
        dir = uniform(0,2*PI)
        e = asteroid_creator.create(sides, radix, x0, y0, speed, dir)
        asteroids.append(e)


def keyPressed():
    if keyCode == UP:
        sc.speed_up()
        spacecraft_drawer.draw_fire(sc)
    elif keyCode == DOWN:
        sc.brake()
    elif keyCode == LEFT:
        sc.turn_left()
    elif keyCode == RIGHT:
        sc.turn_right()
    elif keyCode == 32: # Spacebar
        m = sc.shoot();
        missiles.append(m)
    

def clean():
    background(255,255,255)
    

def draw():
    clean()
    sc.update_position(width, height)
    spacecraft_drawer.draw_it(sc)
    for a in asteroids:
        a.update_position(width, height)
        asteroid_drawer.draw_it(a)
    for i, m in enumerate(missiles):
        if m.x > width or m.x < 0 or m.y > height or m.y < 0:
            missiles.pop(i)
        print(missiles)
        m.update_position(width, height)
        missile_drawer.draw_it(m)
