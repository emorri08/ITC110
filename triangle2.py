#triangle2.py
# new version of the triangle program
# add: calculate the parameter

from math import *
from graphics import *

def square(x):
    return x * x

def distance(p1,p2):
    dist = (square(p2.getX() - p1.getX())) + (square(p2.getY() - p1.getY()))
    return dist

def drawTriangle():
    win = GraphWin("Draw Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5,0.5), "Click on three points")
    message.draw(win)

    #get and draw the vertices of the triangle
    p1 = win.getMouse()
    p1.draw(win)
-
    p2 = win.getMouse()
    p2.draw(win)

    p3 = win.getMouse()
    p3.draw(win)

    #draw a triangle with a polygon object
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("Dark Violet")
    triangle.setOutline("Orange")
    triangle.draw(win)

    #calculate the perimeter
    perim = distance(p1,p2) + distance(p2,p3) + distance(p3,p1)
    message.setText("The perimeter is: {0:0.2f}-".format(perim,))

    #close the window
    win.getMouse()
    win.close()

def main():
    drawTriangle()

main()