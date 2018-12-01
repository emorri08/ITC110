#rectangle.py
# first class

class Rectangle:
    #constructor method
    def __init__ (self, height, width, description):
        self.height = height
        self.width = width
        self.description = description

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * self.height + 2 * self.width

    def scaleSize(self, scale):
        self.height = self.height * scale
        self.width = self.width * scale
    
    def setDescription(self, description):
        self.description = description

    def setHeight(self, height):
        self.height = height
    
    def setWidth(self, width):
        self.width = width
    

#create an instance of a rect object
rect1 = Rectangle(100, 45, "Skinny Rectangle")

print("Area:",rect1.area())

print("Perimeter:",rect1.perimeter())

rect1.scaleSize(0.5)

print("Area:", rect1.area())

rect1.setDescription("A tiny rectangle")

print(rect1.description)

#create a second rectangle
rect2 = Rectangle(50,50,"Perfect Square")

print("Area:", rect2.area())

print("Perimeter:", rect2.perimeter())

rect2.scaleSize(2)
print("Scaled Area:", rect2.area())

rect2.setDescription("I used to be by the window and I could see the squirrels and they were married....")
print(rect2.description)

rect2.setHeight(100)

rect2.setWidth(300)

rect2.setDescription("not so perfect anymore....")
print(rect2.description)