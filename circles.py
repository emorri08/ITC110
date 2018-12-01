#circles.py
from graphics import *

def main():
    win = GraphWin("Eyes")

    #Incorrect way
    #doesn't work because these are not simple variables...
    #they are objects and cant assign one value to the
    #other. have to create both eyes.
    
    '''
    leftEye = Circle(Point(80,50), 5)
    leftEye.setFill("Yellow")
    leftEye.setOutline("Red")
    leftEye.draw(win)

    rightEye = leftEye
    rightEye.move(20,0)
    rightEye.draw(win)
    '''

    #correct but inefficient solution
    '''
    leftEye = Circle(Point(80,50), 5)
    leftEye.setFill("Yellow")
    leftEye.setOutline("Red")
    leftEye.draw(win)

    rightEye = Circle(Point(100,50), 5)
    rightEye.setFill("Yellow")
    rightEye.setOutline("Red")
    rightEye.draw(win)
    '''

    #clone the left eye to make a right eye
    leftEye = Circle(Point(80,50), 10)
    leftEye.setFill("Yellow")
    leftEye.setOutline("Red")
    leftEye.draw(win)

    rightEye = leftEye.clone()
    rightEye.move(40, 0)
    rightEye.draw(win)

main()
