from OpenGL.GL import *
from OpenGL.GLUT import *


RED = (1.0, 0.0, 0.0)
GREEN = (0.0, 1.0, 0.0)
BLUE = (0.0, 0.0, 1.0)

degrees = {
    0: 0,
    1: 90,
    2: 180,
    3: 270,
}


def mirror(iterable):
    return iterable + [(-v[0], v[1]) for v in iterable[::-1]]


class Object(object):
    mode = GL_POLYGON

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
            glBegin(self.mode)
            for x, y in self.vertices:
                glVertex3f(x, y, 0)
            glEnd()
        if hasattr(self, 'objects'):
            for item, x, y in self.objects:
                glTranslated(x, y, 0)
                item.draw()


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
    color = (1, 1, 1)
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
    rotate = 0
    mirror = False

    def __init__(self, x, y, color=BLUE):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        c = self.centroide()
        glLoadIdentity()
        glTranslated(self.x + c[0], self.y + c[1], 0)
        if self.mirror:
            glScaled(-1, 1, 1)
        glRotate(degrees[self.rotate], 0, 0, 1)
        glTranslated(-c[0], -c[1], 0)
        super(Car, self).draw()


class Arrow(Object):
    color = RED
    vertices = [
        (10.0, 0.0),
        (10.0, 20.0),
        (0.0, 30.0),
        (-10.0, 20.0),
        (-10.0, 0.0),
    ]
