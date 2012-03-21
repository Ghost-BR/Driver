from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from base import *


def level():
    glLoadIdentity()
    
    glTranslated(0, 50, 0)
    for _ in range(15):
        glTranslated(20, 0, 0)
        tree.draw()
    
    glTranslated(50, 0, 0)
    for _ in range(13):
        glTranslated(20, 0, 0)
        tree.draw()

    glLoadIdentity()
    glTranslated(300, 55, 0)
    for _ in range(9):
        glTranslated(0, 20, 0)
        tree.draw()

    glLoadIdentity()
    glTranslated(340, 320, 0)
    house.draw()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    level()
    car.draw()
    
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
        car.rotate = 1
    elif k == GLUT_KEY_DOWN:
        car.y -= 5.0
        car.rotate = 3
    elif k == GLUT_KEY_LEFT:
        car.x -= 5.0
        car.rotate = 2
    elif k == GLUT_KEY_RIGHT:
        car.x += 5.0
        car.rotate = 0
    else:
        return
    glutPostRedisplay()


if __name__ == '__main__':
    house = House()
    tree = Tree()
    car = Car(20, 30)

    base(display, reshape, keyboard, special)
