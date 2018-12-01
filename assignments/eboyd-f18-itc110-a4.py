#eboyd-f18-itc110-a4.py
#   This program draws a picture of a truck in a graphics window

from graphics import *

def main():
    #create the graphics window and set coordinates so it's easier to work with.
    win = GraphWin("EBoyd A4 Truck",400,400)
    win.setCoords(0.0,0.0,10.0,10.0)

    #create and draw the body of the Truck
    truckBody = Rectangle(Point(1.0,7.5),Point(6.5,3.0))
    truckBody.setFill("Red")
    truckBody.setOutline("Red")
    truckBody.draw(win)

    #create and draw the cab of the truck
    truckCab = Rectangle(Point(6.5,6.0), Point(8.5,3.0))
    truckCab.setFill("Red")
    truckCab.setOutline("Red")
    truckCab.draw(win)

    #create and draw a window in the cab of the truck
    truckWin = Rectangle(Point(7.2,5.7),Point(8.2,4.7))
    truckWin.setFill("Light Gray")
    truckWin.setOutline("Black")
    truckWin.draw(win)

    #create and draw the front wheel well
    frontWell = Circle(Point(7,2.8),1)
    frontWell.setFill("White")
    frontWell.setOutline("White")
    frontWell.draw(win)

    #create and draw the front tire
    frontTire = Circle(Point(7,2.8),0.9)
    frontTire.setFill("Black")
    frontTire.setOutline("Black")
    frontTire.draw(win)

    #create and draw the rear wheel well
    rearWell = Circle(Point(2.5,2.8),1)
    rearWell.setFill("White")
    rearWell.setOutline("White")
    rearWell.draw(win)

    #create and draw the rear tire
    rearTire = Circle(Point(2.5,2.8),0.9)
    rearTire.setFill("Black")
    rearTire.setOutline("Black")
    rearTire.draw(win)

    #create and draw the rear bumper
    rearBump = Rectangle(Point(0.7,3.5),Point(1.1,2.9))
    rearBump.setFill("Slate Gray")
    rearBump.setOutline("Slate Gray")
    rearBump.draw(win)

    #create and draw the front bumper
    frontBump = Rectangle(Point(8.4,3.5),Point(8.8,2.9))
    frontBump.setFill("Slate Gray")
    frontBump.setOutline("Slate Gray")
    frontBump.draw(win)

    #quit button
    quitButton = Rectangle(Point(4.4,.8),Point(5.6,.2))
    quitButton.setFill("gray")
    quitButton.draw(win)
    msg = Text(Point(5,.5),"QUIT").draw(win)

    # wait for a mouse click to close graphics window
    win.getMouse()
    win.close()

main()
