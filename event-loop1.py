#event-loop1.py
# changes color of the window with keyboard controls

from graphics import *

def main():
    win = GraphWin("Color Window", 500, 500)

    #create the event loop to handle key presses
    # until the user presses "q" key

    while True:
        key = win.getKey()
        if key == "q": #exit the loop
            break #break the loop
        #process the key
        if key == "r":
            win.setBackground("Deep Pink")
        elif key == "w":
            win.setBackground("White")
        elif key == "g":
            win.setBackground("Lime Green")
        elif key == "b":
            win.setBackground("Sky Blue")
        elif key == "x":
            win.setBackground("Black")
        elif key == "y":
            win.setBackground("Yellow")
        elif key == "f":
            win.setBackground("Fuchsia")
        elif key == "o":
            win.setBackground("Orange")
        elif key == "v":
            win.setBackground("Brown")
        elif key == "t":
            win.setBackground("Turquoise")
        elif key == "p":
            win.setBackground("Purple")
    #exit the program
    win.close()

main()