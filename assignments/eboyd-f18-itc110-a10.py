#eboyd-f18-itc110-a10.py
# cat class

class Cat:
    #constructor
    def __init__(self, name, age, breed, color):
        #instance variables
        self.name = name
        self.age = float(age)
        self.breed = breed
        self.color = color
    
    #accessor methods
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getBreed(self):
        return self.breed

    def getColor(self):
        return self.color
    
    def getHumYrs(self):
        return self.age * 7

def main():
    #create some kitties
    kitty1 = Cat("Gaucho", 7, "Domestic Short-hair", "Brown Tabby")
    kitty2 = Cat("Salsa", 7, "Domestic Short-hair", "Torbie")
    kitty3 = Cat("Abby", 12, "Domestic Short-hair", "Silver Tabby")
    kitty4 = Cat("Ellie Cat", 15, "Domestic Long-hair", "Tuxedo")
    kitty5 = Cat("Panda", 8, "Domestic Short-hair", "Tuxedo")
    kitty6 = Cat("Tippy", 3, "Domestic Medium-hair", "Tuxedo")
    kitty7 = Cat("Sweetie", 3, "Domestic Short-hair", "Tuxedo")
    kitty8 = Cat("Corra", 4, "Maine Coon", "Dilute Calico")
    kitty9 = Cat("Pounce", 4, "Maine Coon", "Grey and White Tuxedo")
    kitty10 = Cat("Captain", 8, "Maine Coon", "Brown Tabby")

    #display kitties
    print("The first cat is", kitty1.getName())
    print("Age:", kitty1.getAge(), "years old.")
    print("Color:", kitty1.getColor())
    print("Breed:", kitty1.getBreed())
    print("Age (human yrs):", kitty1.getHumYrs(), "years old.")
    print(" ")

    print("The second cat is", kitty2.getName())
    print("Age:", kitty2.getAge(), "years old.")
    print("Color:", kitty2.getColor())
    print("Breed:", kitty2.getBreed())
    print("Age (human yrs):", kitty2.getHumYrs(), "years old.")
    print(" ")

    print("The third cat is", kitty3.getName())
    print("Age:", kitty3.getAge(), "years old.")
    print("Color:", kitty3.getColor())
    print("Breed:", kitty3.getBreed())
    print("Age (human yrs):", kitty3.getHumYrs(), "years old.")
    print(" ")

    print("The fourth cat is", kitty4.getName())
    print("Age:", kitty4.getAge(), "years old.")
    print("Color:", kitty4.getColor())
    print("Breed:", kitty4.getBreed())
    print("Age (human yrs):", kitty4.getHumYrs(), "years old.")
    print(" ")

    print("The fifth cat is", kitty5.getName())
    print("Age:", kitty5.getAge(), "years old.")
    print("Color:", kitty5.getColor())
    print("Breed:", kitty5.getBreed())
    print("Age (human yrs):", kitty5.getHumYrs(), "years old.")
    print(" ")

    print("The sixth cat is", kitty6.getName())
    print("Age:", kitty6.getAge(), "years old.")
    print("Color:", kitty6.getColor())
    print("Breed:", kitty6.getBreed())
    print("Age (human yrs):", kitty6.getHumYrs(), "years old.")
    print(" ")

    print("The seventh cat is", kitty7.getName())
    print("Age:", kitty7.getAge(), "years old.")
    print("Color:", kitty7.getColor())
    print("Breed:", kitty7.getBreed())
    print("Age (human yrs):", kitty7.getHumYrs(), "years old.")
    print(" ")

    print("The eighth cat is", kitty8.getName())
    print("Age:", kitty8.getAge(), "years old.")
    print("Color:", kitty8.getColor())
    print("Breed:", kitty8.getBreed())
    print("Age (human yrs):", kitty8.getHumYrs(), "years old.")
    print(" ")

    print("The ninth cat is", kitty9.getName())
    print("Age:", kitty9.getAge(), "years old.")
    print("Color:", kitty9.getColor())
    print("Breed:", kitty9.getBreed())
    print("Age (human yrs):", kitty9.getHumYrs(), "years old.")
    print(" ")

    print("The tenth cat is", kitty10.getName())
    print("Age:", kitty10.getAge(), "years old.")
    print("Color:", kitty10.getColor())
    print("Breed:", kitty10.getBreed())
    print("Age (human yrs):", kitty10.getHumYrs(), "years old.")
    print(" ")

main()
