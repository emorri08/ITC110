#basic tests with graphics

from graphics import * #gives access to all functions in graphics library

def main():
    #create a window object
    win = GraphWin("First Window", 640, 400)
    #create a point
    p1 = Point(50,60)
    p1.draw(win)
    print(p1.getX())
    #create a second point
    p2 = Point(100,150)
    p2.draw(win)
    #create a line connecting points
    line = Line(p1,p2)
    line.setFill("green")
    line.setWidth(3)
    line.draw(win)

main()
