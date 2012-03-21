from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from base import base

RED = (1.0, 0.0, 0.0)
GREEN = (0.0, 1.0, 0.0)
BLUE = (0.0, 0.0, 1.0)


def mirror(iterable):
        return iterable + [(-v[0], v[1]) for v in iterable[::-1]]


class Object(object):
    
    def centroide(self):
        x_total = 0
        y_total = 0
        len_ = len(self.vertices)
        for x, y in self.vertices:
            x_total += x
            y_total += y
        return  (x_total / len_, y_total / len_) 
    
    def draw(self):
        if hasattr(self, 'color'):
            glColor3f(*self.color)
        if hasattr(self, 'vertices'):
            glBegin(GL_POLYGON)
            for x, y in self.vertices:
                glVertex3f(x, y, 0)
            glEnd()
        if hasattr(self, 'objects'):
            for item, x, y in self.objects:
                glTranslated(x, y, 0);
                item.draw()


class House(Object):

    color = RED

    vertices = [
        (10.0, 0.0),
        (10.0, 20.0),
        (0.0, 30.0),
        (-10.0, 20.0),
        (-10.0, 0.0),
    ]

class Tree(Object):

    color = GREEN

    vertices = mirror([
        (-5, 50),
        (-15, 40),
        (-15, 30),
        (-5, 20),
        (-5, 0),
    ])


class Wheel(Object):
    
    vertices = mirror([
            (-2.5, 5),
            (-5, 2.5),
            (-5, -2.5),
            (-2.5, -5),
        ])


class Car(Object):

    vertices = mirror([
        (-10, 25),
        (-15, 15),
        (-30, 15),
        (-30, 5),
    ])
        
    objects = [
        (Wheel(), -20, 5),
        (Wheel(), 40, 0),
    ]

    def __init__(self, x, y, color=BLUE):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        glLoadIdentity()
        glTranslated(self.x, self.y, 0);
        super(Car, self).draw()


def level():
    glLoadIdentity()
    
    glTranslated(50, 50, 0);
    house.draw()
    
    glTranslated(20, 0, 0);
    tree.draw() 


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    level()
    car.draw()

    #glLoadIdentity()
    #glTranslated(0, 480, 0)
    #glRotated(180, 0, 0, 1)
    #house.draw()
    
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)
    glMatrixMode(GL_MODELVIEW)

def keyboard(k, x, y):
    # If esc is pressed, exit.
    if ord(k) == 27:
        sys.exit()

def special(k, x, y):
    global car

    if k == GLUT_KEY_UP:
        car.y += 5.0
    elif k == GLUT_KEY_DOWN:
        car.y -= 5.0
    elif k == GLUT_KEY_LEFT:
        car.x -= 5.0
    elif k == GLUT_KEY_RIGHT:
        car.x += 5.0
    else:
        return
    glutPostRedisplay()


house = House()
tree = Tree()
car = Car(20, 30)

if __name__ == '__main__':
    base(display, reshape, keyboard, special)