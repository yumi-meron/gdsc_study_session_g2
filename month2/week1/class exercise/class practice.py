# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.
#     def say_name(self):
#         return f"My name is {self.name}"
# p1 = Person("meron", 20)
# print(p1.say_name())


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def calc_area(self):
#         return 3.14 * self.radius
# c1 = Circle(2)
# print(c1.calc_area())

# class Rectangle():
#     def __init__(self, length, width) -> None:
#         self.length = length
#         self.width = width
#     def calc_area(self):
#         return f"The area of the Rectangle is {self.length * self.width}"
    
#     def calc_perimeter(self):
#         return f"The perimeter of the Rectangle is {2*(self.length + self.width)}"
# R1 = Rectangle(3.2,5.5)
# print(R1.calc_area())
# print(R1.calc_perimeter())
from abc import ABC, abstractmethod
class Shape(ABC):
    def __init__(self, color):
        self.color = color
    def show_color(self):
        return self.color
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,color, radius):
        super().__init__(color)
        self.radius = radius
    def area(self):
        return f"The area of the circle is {3.14 *(self.radius ** 2)}"

class Rectangle(Shape):
    def __init__(self,color,length, width):
        super().__init__(color)
        self.length = length
        self.width = width
    def area(self):
        return f"The area of the Rectangle is {self.length * self.width}"
    def peri(self):
        return f"The perimeter of the Rectangle is {2*(self.length + self.width)}"
    
r1 = Rectangle("Blue",2,5)
print(r1.show_color())
print(r1.area())
print(r1.peri())

c1 = Circle("Yellow", 5)
print(c1.show_color())
print(c1.area())






    
