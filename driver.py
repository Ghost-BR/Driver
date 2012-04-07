from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from model import *


arrow = Arrow()
tree = Tree()
car = Car(20, 30)


def florest(x, y, rows, columns):
    glLoadIdentity()

    glTranslated(x, y, 0)
    for i in range(rows):
        for _ in range(columns):
            tree.draw()
            glTranslated(25, 0, 0)
        glLoadIdentity()
        glTranslated(x, i * 30 + y, 0)


def level():
    florest(20, 50, 4, 11)
    florest(20, 140, 8, 1)
    florest(20, 350, 4, 24)
    florest(370, 50, 11, 10)

    glLoadIdentity()
    glTranslated(110, 190, 0)
    arrow.draw()

    c = arrow.centroide()

    glLoadIdentity()
    glTranslated(110 + c[0], 290 + c[1], 0)
    glRotated(180, 0, 0, 1)
    glScaled(2, 2, 1)
    glTranslated(-c[0], -c[1], 0)
    arrow.draw()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    level()
    car.draw()

    glutSwapBuffers()


def reshape(width, height):
    glClearColor(0.4, 0.2, 0.0, 0.0)
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

    mirror = False
    rotate = 0
    if k == GLUT_KEY_UP:
        car.y += 5.0
        rotate = 1
        if car.y > 480:
            car.y = 0
    elif k == GLUT_KEY_DOWN:
        car.y -= 5.0
        rotate = 3
        if car.y < 0:
            car.y = 480
    elif k == GLUT_KEY_LEFT:
        car.x -= 5.0
        mirror = True
        if car.x < 0:
            car.x = 640
    elif k == GLUT_KEY_RIGHT:
        car.x += 5.0
        if car.x > 640:
            car.x = 0
    else:
        return
    car.rotate = rotate
    car.mirror = mirror
    glutPostRedisplay()


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

    glutInitWindowPosition(0, 0)
    glutInitWindowSize(640, 480)
    glutCreateWindow('Driver')

    #callbacks
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special)

    #mainloop
    glutMainLoop()
