class Person():
    def __init__(self, nationality, name):
        self.name = name
        self.nationality = nationality

    def printInfo(self):
        print("Name:", self.name)
        print("Natioality:", self.nationality)

    def setSurname(self, surname):
        self.surname = surname

    def getSurname(self):
        return self.surname
class Student(Person):
    def __init__(self, nationality, name, id):
        super().__init__(name, nationality)
        self.id = id
    def printInfo(self):
        super().printInfo()
        print("Id:", self.id)

student = Student("Madina", "Kazakh", "22B080555")
print(student.printInfo())

class Teacher(Person):
    def __init__(self, name, nationality, teacher_id):
        super().__init__(name, nationality)
        self.teacher_id = teacher_id
    def printInfo(self):
        super().printInfo()
        print("Teacher's name:", self.name)
        print("Teacher's nationality:", self.nationality)
        print("Teacher's id:", self.teacher_id)
teacher = Teacher("Arnur", "Kazakh", "32334545")
print(teacher.printInfo())