#triangle.pyw
from graphics import *

def main():
    w = GraphWin("Draw A Triangle")
    w.setCoords(0.0, 0.0, 10.0, 10.0)
    msg = Text(Point(5,0.5), "Click on three points")
    msg.draw(w)

    #draw the three vertices of the triangle
    p1 = w.getMouse()
    p1.draw(w)

    p2 = w.getMouse()
    p2.draw(w)

    p3 = w.getMouse()
    p3.draw(w)

    #use a polygon to draw a triangle
    tri = Polygon(p1,p2,p3)
    tri.setFill("dark violet")
    tri.setOutline("goldenrod")
    tri.draw(w)

    #wait for user to click to  exit
    msg.setText("Click anywhere to exit")
    w.getMouse()
    w.close()

main()
