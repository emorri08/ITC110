#event-loop3.py
# change window color and use clicks
# to enter text

from graphics import *

#change background colors based on key input from user
def handleKey(k, win):
    #process the key
    if k == "r":
        win.setBackground("Deep Pink")
    elif k == "w":
        win.setBackground("White")
    elif k == "g":
        win.setBackground("Lime Green")
    elif k == "b":
        win.setBackground("Sky Blue")
    elif k == "x":
        win.setBackground("Black")
    elif k == "y":
        win.setBackground("Yellow")
    elif k == "f":
        win.setBackground("Fuchsia")
    elif k == "o":
        win.setBackground("Orange")
    elif k == "v":
        win.setBackground("Brown")
    elif k == "t":
        win.setBackground("Turquoise")
    elif k == "p":
        win.setBackground("Purple")

#create Entry object, waits for user to Return
#converts it to text and draws it on the window
def handleClick(pt, win):
    #create an entry object for the user to type in
    entry = Entry(pt, 10)
    entry.draw(win)

    #wait until user presses Return or Esc key
    while True:
        key = win.getKey()
        if key == "Return":
            break
    #undraw the entry and draw the text
    entry.undraw()
    Text(pt, entry.getText()).draw(win)


    #clear any mouse clicks that might have occured
    #during text entry
    win.checkMouse()

def main():
    win = GraphWin("Click and Type", 500, 500)
    
    #event loop
    while True:
        key = win.checkKey() #check the key the user entered
        if key == "q": #quit
            break
        
        if key: #handle key
            handleKey(key, win)

        pt = win.checkMouse()
        if pt: #handle click
            handleClick(pt, win)

    win.close()

main()