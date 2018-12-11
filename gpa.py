#gpa.py

#create the class
class Student:
    #constructor
    def __init__(self, name, hours, qpoints):
        #instance variables (special variables that belong to the class)
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
    
    #accessor methods (look up mutator methods)
    def getName(self):
        return self.name
    
    def getHours(self):
        return self.hours
    
    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours

#create the student object with data from the file
def makeStudent(infoStr):
    #infoStr is a tab separated line: name, hours, qpoints
    #return the student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def main():
    #open the file for reading
    filename = input("Enter the file name with grades: ")
    infile = open(filename, "r")
    #making a student object with info from the file
    #this is current best
    best = makeStudent(infile.readline())

    #loop through each student
    #compare with current best
    #find the best in the file
    for line in infile:
        s = makeStudent(line)
        if s.gpa() > best.gpa():
            best = s
    #close the file
    infile.close()
    #display the student with the best GPA
    print("The best student is:", best.getName())
    print("Hours:", best.getHours())
    print("GPA:", best.gpa())

main()