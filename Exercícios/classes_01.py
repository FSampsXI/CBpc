class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_student(self):
        print(f"{self.name} is {self.age} years old and your grade is {self.grade}")



g = Student("Fernando", 20, 8)
g.get_student()