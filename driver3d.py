from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from model import *


droid = Droid()

rot_x = 0.0
rot_y = 0.0
rot_z = 0.0


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    glRotatef(rot_x, 1.0, 0.0, 0.0)
    glRotatef(rot_y, 0.0, 1.0, 0.0)
    glRotatef(rot_z, 0.0, 0.0, 1.0)
    droid.draw()

    glutSwapBuffers()


def reshape(width, height):
    h = float(height) / float(width)

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -h, h, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)


def keyboard(k, x, y):
    # If esc is pressed, exit.
    if ord(k) == 27:
        sys.exit()


def special(k, x, y):
    global rot_x, rot_y, rot_z

    if k == GLUT_KEY_UP:
        rot_x += 1
    elif k == GLUT_KEY_DOWN:
        rot_x -= 1
    elif k == GLUT_KEY_LEFT:
        rot_y += 1
    elif k == GLUT_KEY_RIGHT:
        rot_y -= 1
    else:
        return
    glutPostRedisplay()


if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)

    glutInitWindowPosition(0, 0)
    glutInitWindowSize(640, 480)
    glutCreateWindow('Spheres')

    #callbacks
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special)

    #mainloop
    glutMainLoop()
