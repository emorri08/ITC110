#eboyd-f18-itc110-a1.py
# use functions to draw faces

from graphics import *

def createWindow():
    #create graphics window
    window = GraphWin("Smiley Faces",400,400)
    #change the background color of the window
    window.setBackground("Black")
    #set the coordinates from 0,0 in lower left to 20,20 in upper right
    window.setCoords(0.0,0.0,20.0,20.0)
    return window

def drawFace(center, size, window):
    #create the head
    face = Circle(center, size)
    face.setFill("Yellow")
    face.draw(window)

def drawEye(center, size, window):
    #create the eyes
    eyes = Circle(center, size)
    eyes.draw(window)

def drawMouth(start, end, window):
    #create the mouth
    mouth = Line(start, end)
    mouth.draw(window)

def quitButton(point1, point2, window):
    #create a quit "button
    button = Rectangle(point1,point2)
    button.setFill("Grey")
    button.draw(window)
    Text(Point(10, 1.5),"QUIT").draw(window)

def main():
    #create the window
    win = createWindow()

    #draw face one - smallest face.
    drawFace(Point(5, 5), 1, win)
    drawEye(Point(4.5, 5.25), 0.15, win)
    drawEye(Point(5.5, 5.25), 0.15, win)
    drawMouth(Point(4.5, 4.5), Point(5.5, 4.5), win)

    #draw face two - medium sized face.
    drawFace(Point(10,10), 1.5, win)
    drawEye(Point(9.5, 10.5), 0.2, win)
    drawEye(Point(10.5, 10.5), 0.2, win)
    drawMouth(Point(9.25, 9.25), Point(10.75, 9.25), win)
    
    #draw face three - largest face.
    drawFace(Point(15, 15), 2, win)
    drawEye(Point(14.5, 16), 0.25, win)
    drawEye(Point(15.5, 16), 0.25, win)
    drawMouth(Point(14, 14), Point(16, 14), win)

    #quit button
    quitButton(Point(9, 2), Point(11, 1), win)
    win.getMouse()
    win.close()

main()