#convert-gui.py
# convert Celsius to Fahrenheit with the use of a Gui

from graphics import *

def main():
    
    win = GraphWin("Temp Converter",400,300)
    win.setCoords(0.0,0.0,3.0,4.0)

    #draw the interface
    Text(Point(1,3),"Celsius Temp").draw(win)
    Text(Point(1,1),"Fahrenheit Temp").draw(win)
    inputText = Entry(Point(2.25,3),5)
    inputText.setText("0.0")
    inputText.draw(win)

    outputText = Text(Point(2.25,1), "")
    outputText.draw(win)

    rect = Rectangle(Point(1,1.5),Point(2,2.5))
    rect.setFill("dark violet")
    rect.draw(win)
    button = Text(Point(1.5,2.0),"Convert it!").draw(win)

    #wait for mouse click
    win.getMouse()

    #convert the input
    celsius = float(inputText.getText())
    fahrenheit = 9.0 / 5.0 * celsius + 32

    #display output and change button text
    outputText.setText(round(fahrenheit,2))
    button.setText("Quit!")

    #quit the program
    win.getMouse()
    win.close()
         
main()
