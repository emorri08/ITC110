#click.py (in class)

from graphics import *

def main():
    win = GraphWin("Click Me")

    for i in range(10):
        #returns a point where the mouse was clicked
        p = win.getMouse()
        print("you clicked at", p.getX(), p.getY())

main()