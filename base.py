from OpenGL.GLUT import *

def base(display, reshape, keyboard=None, special=None, idle=None):
    #Init Glut
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    
    #create window
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(640, 480)
    glutCreateWindow('Houses')
    
    #callbacks
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    if keyboard is not None:
        glutKeyboardFunc(keyboard)
    if special is not None:
        glutSpecialFunc(special)
    if idle is None:
        glutIdleFunc(display)
    else:
        glutIdleFunc(idle)
    
    #mainloop
    glutMainLoop()