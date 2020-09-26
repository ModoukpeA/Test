#This program calculates the total marks of a student and the associated percentage

class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalMarks(self):
        return (self.phy + self.chem + self.bio)
    def Percentage(self):
        return ((self.totalMarks()/300) * 100)

obj1 = Student("Iris", 100, 90, 80)
print(obj1.totalMarks())
print(obj1.Percentage())