# c06ex15.py
#   face drawing program

from graphics import *

def drawFace(center, size, window):
    
    eyeSize = .15 * size
    eyeOff = size / 3.0
    mouthSize = 0.8 * size
    mouthOff = size / 2.0
    head = Circle(center, size)
    head.setFill("Yellow")
    head.draw(window)
    leftEye = Circle(center, eyeSize)
    leftEye.move(-eyeOff, -eyeOff)
    rightEye = Circle(center,eyeSize)
    rightEye.move(eyeOff, eyeOff)
    