# Desenvolva uma classe Book com atributos title, author e year. 
# Implemente um método get_age que retorna quantos anos o 
# livro tem desde o ano atual.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def get_age(self, actual_year):
        self.actual_year = input(("Enter the current year: "))
        return actual_year
        print(f"The book is {self.title} by author {self.author}, written in year {self.year}")
        print(f"It's been {self.year - } years since it was written in")

n = Book("O Cão de Baskerville", "Arthur Conan Doyle", 1912)
n.get_age(
