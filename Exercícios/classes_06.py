# Crie uma classe Student com atributos name, age e grades (uma lista).
# Adicione métodos para adicionar notas, calcular a média das notas e exibir as informações do aluno.


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if len(self.grades):
            total = sum(self.grades)
            average = total / len(self.grades)
            return average
        else:
            return 0
    
    def display_info(self):
        print(f"Nome: {self.name}")
        print(f"Idade: {self.age}")
        print(f"Notas: {self.grades}")
        print(f"Média: {self.calculate_average()}")

aluno = Student("João", 20)
aluno.add_grade(8)
aluno.add_grade(7)
aluno.add_grade(9)
aluno.display_info()
    