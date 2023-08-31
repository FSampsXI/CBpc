# Desenvolva uma classe Rectangle com atributos width e height.
# Implemente um método calculate_area para calcular e retornar a área do retângulo.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        print(f'Width: {self.width}')
        print(f'Height: {self.height}')
        return self.width * self.height

area_rectangle = Rectangle(5, 10)
area = area_rectangle.calculate_area()

print(f'The area of the rectangle is: {area}')