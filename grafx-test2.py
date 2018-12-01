# grafx-test2.py

from graphics import *

def main():

    #open a graphics window - creating a window object
    win = GraphWin("Shapes", 400, 400)#doesn't have to be win, but should make sense - also...the "400, 400" changes the size of the window from the default size of 200 by 200

    #create a circle
    center = Point(75,100)
    circ = Circle(center, 80)
    #make the circle pretty
    circ.setFill("dark violet")

    #create a bonus circle
    center2 = Point(150,150)
    circ2 = Circle(center2, 70)
    #make bonus  circle pretty
    circ2.setFill("deep pink")

    #draw circles in window
    circ.draw(win)
    circ2.draw(win)

    #add some text to the first circle
    label = Text(Point(57,100), "Purple Circle")
    label.draw(win)

    #add some text to the second circle
    label2 = Text(Point(150,150), "Pink circle")
    label2.draw(win)

    #create a rectangle
    rect = Rectangle(Point(30,30), Point(70,70))
    #make the rectangle pretty
    rect.setFill('aqua')
    #draw the rectangle in the window
    rect.draw(win)

    #create and draw a line
    line = Line(Point(20,30), Point(180,165))
    line.draw(win)

    #create and draw an oval
    oval = Oval(Point(20,350), Point(380,399))
    oval.setFill("spring green")
    oval.draw(win)
    
main()
