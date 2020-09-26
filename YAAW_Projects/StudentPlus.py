class Student:
    def setName(self, name):
        self.__name = name

    def getName(self):
        return (self.__name)

    def setRollNumber(self, RollNumber):
        self.__RollNumber = RollNumber

    def getRollNumber(self):
        return (self.__RollNumber)

obj1 = Student()
obj1.setName("Toto")
obj1.setRollNumber(1000)
print(obj1.getName())
print(obj1.getRollNumber())

