class Person():
    def __init__(self, name, nationallity):
        self.name = name
        self.nationallity = nationallity
    def printInfo(self):
        print('Name:', self.name)
        print('Nationallity:', self.nationallity)
    def setSurname(self, surname):
        self.surname = surname
    def getSurname(self):
        return self.surname
    
class Student(Person):
    def __init__(self, name, nationallity, id):
        super().__init__(name, nationallity)
        self.id = id
        
    def printInfo(self):
        super().printInfo()
        print('Id:', self.id)
stud = Student("Madina", "Kazakh", "22B050855")
print(stud.printInfo())

class Teacher(Person):
    def __init__(self, name, nationality, teacher_id):
        super().__init__()(name, name, nationality)
        self.id = id

    def printInfo(self):
        super().printInfo()
        print("teacher's name: " + self.nationality)
        print("teacher's nationality: " + self.nationality)
        print("teacher's id " + self.teacher_id)

teacher = Teacher("Arnur", "kazakh", "226756756757")
print(teacher.info())
        