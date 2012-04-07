from OpenGL.GL import *
from OpenGL.GLUT import *


class Droid(object):

    def __init__(self):
        self.angle = 0.0
        self.left_leg = {
            'pos': [-0.15, -0.35, 0.0],
            'angle': 0.0,
            'move': False,
            'foot': {
                'pos': [0.0, -0.2, 0.0],
                'angle': 0.0,
            }
        }

        self.right_leg = {
            'pos': [0.15, -0.35, 0.0],
            'angle': 0.0,
            'move': False,
            'foot': {
                'pos': [0.0, -0.2, 0.0],
                'angle': 0.0,
            }
        }

        self.state = 0

    def draw(self):
        glColor3f(1.0, 0.0, 0.0)
        glPushMatrix()

        #body
        glRotatef(self.angle, 1.0, 0.0, 0.0)
        glTranslatef(0.0, 0.2, 0.0)
        glutWireCube(0.5)

        for leg in (self.left_leg, self.right_leg):
            #top
            glPushMatrix()
            glRotatef(leg['angle'], 1.0, 0.0, 0.0)
            glTranslatef(*leg['pos'])
            glutWireCube(0.2)

            #botton
            glTranslatef(*leg['foot']['pos'])
            glutWireCube(0.2)
            glPopMatrix()

        glPopMatrix()

    def walk(self):
        body_angle = 0.2
        leg_angle = 1.0

        if self.state == 0:
            if self.left_leg['angle'] <= 45.0:
                self.angle -= body_angle
                self.left_leg['angle'] += leg_angle
            else:
                self.state = 1

        if self.state == 1:
            if self.left_leg['angle'] > 0.0:
                self.left_leg['angle'] -= leg_angle
                self.angle += body_angle
            else:
                self.state = 2

        if self.state == 2:
            if self.right_leg['angle'] <= 45.0:
                self.angle -= body_angle
                self.right_leg['angle'] += leg_angle
            else:
                self.state = 3
                self.right_leg['move'] = True

        if self.state == 3:
            if self.right_leg['angle'] > 0.0:
                self.right_leg['angle'] -= leg_angle
                self.angle += body_angle
            else:
                self.state = 0

        self.draw()
