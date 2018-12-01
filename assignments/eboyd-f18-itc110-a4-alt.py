#eboyd-f18-itc110-a4-alt.py
#   This program draws a winter scene

from graphics import *

def main():
    #create the graphics window and set coordindates so it's easier to work with
    win = GraphWin("EBoyd A4 Winter Scene",500,500)
    win.setCoords(0.0,0.0,10.0,10.0)

    '''
    BACKGROUND SCENERY
    '''
    #sky
    sky = Rectangle(Point(0,10),Point(10,0))
    sky.setFill("Cyan")
    sky.setOutline("Cyan")
    sky.draw(win)

    #falling snow
    flake1 = Circle(Point(.25,9.8),.075)
    flake1.setFill("Snow")
    flake1.setOutline("Snow")
    flake1.draw(win)

    flake2 = flake1.clone()
    flake2.move(1,-1.2)
    flake2.draw(win)

    flake3 = flake1.clone()
    flake3.move(.125,-2)
    flake3.draw(win)

    flake4 = flake1.clone()
    flake4.move(1.4,-3.15)
    flake4.draw(win)

    flake5 = flake1.clone()
    flake5.move(.5,-5)
    flake5.draw(win)

    flake6  = flake1.clone()
    flake6.move(.1,-6)
    flake6.draw(win)

    flake7 = flake1.clone()
    flake7.move(.75,-7.25)
    flake7.draw(win)

    flake8 = flake1.clone()
    flake8.move(4,0)
    flake8.draw(win)

    flake9 = flake2.clone()
    flake9.move(4,0)
    flake9.draw(win)

    flake10 = flake3.clone()
    flake10.move(4.2,-.3)
    flake10.draw(win)

    flake11 = flake4.clone()
    flake11.move(4.1,-.25)
    flake11.draw(win)

    flake12 = flake5.clone()
    flake12.move(4,0)
    flake12.draw(win)

    flake13 = flake6.clone()
    flake13.move(4.8,-.5)
    flake13.draw(win)

    flake14 = flake8.clone()
    flake14.move(5,-.25)
    flake14.draw(win)

    flake15 = flake9.clone()
    flake15.move(3.5,-.25)
    flake15.draw(win)

    flake16 = flake10.clone()
    flake16.move(4.75,-1)
    flake16.draw(win)

    flake17 = flake12.clone()
    flake17.move(4.45,-1)
    flake17.draw(win)

    #snowy ground
    snow1 = Rectangle(Point(0,2),Point(10,0))
    snow1.setFill("Snow")
    snow1.setOutline("Snow")
    snow1.draw(win)

    #snowy hill
    snow2 = Oval(Point(-2,2.7),Point(12,-2))
    snow2.setFill("Snow")
    snow2.setOutline("Black")
    snow2.draw(win)

    '''
    SNOWPERSON
    '''
    #body
    #bottom of snowperson
    lowBall = Circle(Point(3,3.5),1.5)
    lowBall.setFill("Snow")
    lowBall.setOutline("Snow")
    lowBall.draw(win)

    #center of snowperson
    midBall = Circle(Point(3,6),1.25)
    midBall.setFill("Snow")
    midBall.setOutline("Snow")
    midBall.draw(win)

    #top of snowperson
    topBall = Circle(Point(3,8.1),1)
    topBall.setFill("Snow")
    topBall.setOutline("Snow")
    topBall.draw(win)

    #snowperson's face
    #nose
    nose = Polygon(Point(3,8.11),Point(3,7.89),Point(3.35,8))
    nose.setFill("Orange")
    nose.setOutline("Orange")
    nose.draw(win)

    #left eye
    leftEye = Circle(Point(2.7,8.4),.11)
    leftEye.setFill("Black")
    leftEye.draw(win)

    #right eye
    rightEye = Circle(Point(3.3,8.4),.11)
    rightEye.setFill("Black")
    rightEye.draw(win)

    #mouth
    mouth1 = Circle(Point(2.4,7.9),.05)
    mouth1.setFill("Black")
    mouth1.draw(win)
    
    mouth2 = Circle(Point(3.6,7.9),.05)
    mouth2.setFill("Black")
    mouth2.draw(win)

    mouth3 = Circle(Point(2.6,7.6),.05)
    mouth3.setFill("Black")
    mouth3.draw(win)

    mouth4 = Circle(Point(3.4,7.6),.05)
    mouth4.setFill("Black")
    mouth4.draw(win)

    mouth5 = Circle(Point(3,7.5),.05)
    mouth5.setFill("Black")
    mouth5.draw(win)

    '''
    SNOWPERSON'S ACCESSORIES
    '''
    #brim of hat
    hatBrim = Rectangle(Point(1.8,9.1),Point(4.2,8.8))
    hatBrim.setFill("Black")
    hatBrim.draw(win)

    #top of hat
    topHat = Rectangle(Point(2.25,9.9),Point(3.75,9.1))
    topHat.setFill("Black")
    topHat.draw(win)

    #buttons
    topButton = Circle(Point(3,6.85),.1)
    topButton.setFill("Red")
    topButton.setOutline("Dark Violet")
    topButton.draw(win)

    midButton = Circle(Point(3,6.45),.1)
    midButton.setFill("Red")
    midButton.setOutline("Dark Violet")
    midButton.draw(win)

    lowButton = Circle(Point(3,6.05),.1)
    lowButton.setFill("Red")
    lowButton.setOutline("Dark Violet")
    lowButton.draw(win)

    '''
    TREE
    '''
    #holiday tree
    tri1 = Polygon(Point(8.5,7.6),Point(7.5,9),Point(6.5,7.6))
    tri1.setFill("Forest Green")
    tri1.setOutline("Forest Green")
    tri1.draw(win)

    tri2 = Polygon(Point(7.5,8.3),Point(8.7,6.2),Point(6.3,6.2))
    tri2.setFill("Forest Green")
    tri2.setOutline("Forest Green")
    tri2.draw(win)

    tri3 = Polygon(Point(7.5,7.3),Point(9.1,4.5),Point(5.9,4.5))
    tri3.setFill("Forest Green")
    tri3.setOutline("Forest Green")
    tri3.draw(win)

    tri4 = Polygon(Point(7.5,6),Point(9.5,2.5),Point(5.5,2.5))
    tri4.setFill("Forest Green")
    tri4.setOutline("Forest Green")
    tri4.draw(win)

    #trunk
    trunk = Rectangle(Point(7.2,2.5),Point(7.8,1.8))
    trunk.setFill("Sienna")
    trunk.setOutline("Sienna")
    trunk.draw(win)

    '''
    TREE DECORATIONS
    '''
    #tree-top star
    star = Polygon(Point(7.5,9.6),Point(7.6,9.2),Point(8,9.1),Point(7.6,9),Point(7.5,8.6),Point(7.4,9),Point(7,9.1),Point(7.4,9.2))
    star.setFill("Gold")
    star.setOutline("Goldenrod")
    star.draw(win)

    #lights
    #red lights - diamond shaped
    red1 = Polygon(Point(7.3,8.45),Point(7.4,8.3),Point(7.3,8.15),Point(7.2,8.3))
    red1.setFill("Red")
    #red1.setOutline("Red")
    red1.draw(win)

    red2 = red1.clone()
    red2.move(.8,-.6)
    red2.draw(win)

    red3 = red1.clone()
    red3.move(-.35,-1.2)
    red3.draw(win)

    red4 = red1.clone()
    red4.move(.2,-2)
    red4.draw(win)

    red5 = red1.clone()
    red5.move(-.25,-3.25)
    red5.draw(win)

    red6 = red1.clone()
    red6.move(1,-3.5)
    red6.draw(win)
    
    red7 = red1.clone()
    red7.move(-1.1,-5.5)
    red7.draw(win)

    red8 = red1.clone()
    red8.move(.2,-4.75)
    red8.draw(win)
    
    red9 = red1.clone()
    red9.move(1.3,-5.2)
    red9.draw(win)

    #yellow lights - circle shaped
    yellow1 = Circle(Point(7.8,8.1),.1)
    yellow1.setFill("Yellow")
    #yellow1.setOutline("Yellow")
    yellow1.draw(win)

    yellow2 = yellow1.clone()
    yellow2.move(.5,-1.5)
    yellow2.draw(win)

    yellow3 = yellow1.clone()
    yellow3.move(-.3,-1.1)
    yellow3.draw(win)

    yellow4 = yellow1.clone()
    yellow4.move(-1,-2.4)
    yellow4.draw(win)

    yellow5 = yellow1.clone()
    yellow5.move(-.1,-3.5)
    yellow5.draw(win)

    yellow6 = yellow1.clone()
    yellow6.move(.7,-4.5)
    yellow6.draw(win)

    yellow7 = yellow1.clone()
    yellow7.move(-1.2,-4.2)
    yellow7.draw(win)

    #blue lights - oval shaped
    aqua1 = Oval(Point(6.9,8),Point(7,7.7))
    aqua1.setFill("Deep Sky Blue")
    #aqua1.setOutline("Deep Sky Blue")
    aqua1.draw(win)

    aqua2 = aqua1.clone()
    aqua2.move(.8,-.4)
    aqua2.draw(win)

    aqua3 = aqua1.clone()
    aqua3.move(-.3,-1.4)
    aqua3.draw(win)

    aqua4 = aqua1.clone()
    aqua4.move(-.7,-3.15)
    aqua4.draw(win)

    aqua5 = aqua1.clone()
    aqua5.move(.9,-2.2)
    aqua5.draw(win)

    aqua6 = aqua1.clone()
    aqua6.move(1.7,-2.9)
    aqua6.draw(win)

    aqua7 = aqua1.clone()
    aqua7.move(.6,-3.7)
    aqua7.draw(win)

    aqua8 = aqua1.clone()
    aqua8.move(-.2,-4.55)
    aqua8.draw(win)

    aqua9 = aqua1.clone()
    aqua9.move(.9,-5)
    aqua9.draw(win)

    '''
    QUIT PROGRAM
    '''
    #quit button
    quitButton = Rectangle(Point(4.4,.8),Point(5.6,.2))
    quitButton.setFill("gray")
    quitButton.draw(win)
    msg = Text(Point(5,.5),"QUIT").draw(win)
    #click to quit program
    win.getMouse()
    win.close()

main()