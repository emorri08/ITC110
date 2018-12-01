# c06ex15.py
#   face drawing program

from graphics import *

def drawFace(center, size, window):
    
    head = Circle(center, size)
    head.setFill("yellow")
    head.draw(window)

    eyeSize = 0.15 * size
    eyeOff = size / 3.0
    leftEye = Circle(center, eyeSize)
    leftEye.setFill("Powder Blue")
    leftEye.move(-eyeOff, -eyeOff)
    leftEye.draw(window)

    rightEye = Circle(center, eyeSize)
    rightEye.setFill("Powder Blue")
    rightEye.move(eyeOff, -eyeOff)
    rightEye.draw(window)

    mouthSize = 0.3 * size
    mouth = Circle(center, mouthSize)
    mouth.setFill("Deep Pink")
    mouth.move(0,mouthSize)
    mouth.draw(window)

def test():
    win = GraphWin("Faces")
    win.setBackground("Black")
    drawFace(Point(50,50), 10, win)
    drawFace(Point(100,100), 20, win)
    drawFace(Point(150,150), 30, win)
    win.getMouse()
    win.close()
    
test()