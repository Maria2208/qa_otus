from abc import abstractmethod
from math import pi


class Figure:

    def __init__(self, name):
        self.name = name
        if not isinstance(name, str):
            raise ValueError("Name must be string!")

    @abstractmethod
    def get_area(self):
        """Метод определяет получение площади"""
        raise NotImplementedError("This method is not implemented!")

    def add_area(self, figure):
        """Метод принимает другую геометрическую фигуру и возвращает сумму площадей двух фигур"""
        if not isinstance(figure, Figure):
            print("Error: Invalid class sent")
        else:
            return self.get_area() + figure.get_area()


class Triangle(Figure):
    __angles = 3

    def __init__(self, base, height, first_side, second_side, name):
        super().__init__(name)
        self.base = base
        self.height = height
        self.first_side = first_side
        self.second_side = second_side
        if not isinstance(base, int):
            raise ValueError("base must be integer!")
        elif base < 0:
            raise ValueError("base must be greater than 0!")

        if not isinstance(height, int):
            raise ValueError("height must be integer!")
        elif height < 0:
            raise ValueError("height must be greater than 0!")

        if not isinstance(first_side, int):
            raise ValueError("first_side must be integer!")
        elif first_side < 0:
            raise ValueError("first_side must be greater than 0!")

        if not isinstance(second_side, int):
            raise ValueError("second_side must be integer!")
        elif second_side < 0:
            raise ValueError("second_side must be greater than 0!")

    def get_area(self):
        """Метод получает площадь треугольника"""
        area = 0.5 * self.base * self.height
        return area

    def get_perimeter(self):
        """Метод получает периметр треугольника"""
        perimeter = self.first_side + self.second_side + self.base
        return perimeter


class Rectangle(Figure):
    __angles = 4

    def __init__(self, length, width, name):
        super().__init__(name)
        self.length = length
        self.width = width
        if not isinstance(length, int):
            raise ValueError("length must be integer!")
        elif length < 0:
            raise ValueError("length must be greater than 0!")

        if not isinstance(width, int):
            raise ValueError("width must be integer!")
        elif width < 0:
            raise ValueError("width must be greater than 0!")

    def get_area(self):
        """Метод получает площадь прямоугольника"""
        area = self.length * self.width
        return area

    def get_perimeter(self):
        """Метод получает периметр прямоугольника"""
        perimeter = 2 * (self.length + self.width)
        return perimeter


class Square(Figure):
    __angles = 4

    def __init__(self, side_length, name):
        super().__init__(name)
        self.side_length = side_length
        if not isinstance(side_length, int):
            raise ValueError("side_length must be integer!")
        elif side_length < 0:
            raise ValueError("side_length must be greater than 0!")

    def get_area(self):
        """Метод получает площадь квадрата"""
        area = self.side_length ** 2
        return area

    def get_perimeter(self):
        """Метод получает периметр квадрата"""
        perimeter = 4 * self.side_length
        return perimeter


class Circle(Figure):
    __angles = 0

    def __init__(self, radius, name):
        super().__init__(name)
        self.radius = radius
        if not isinstance(radius, int):
            raise ValueError("Radius must be integer!")
        elif radius < 0:
            raise ValueError("Radius must be greater than 0!")

    def get_area(self):
        """Метод получает площадь круга"""
        area = pi * self.radius ** 2
        return area

    def get_perimeter(self):
        """Метод получает периметр круга"""
        perimeter = 2 * pi * self.radius
        return perimeter


triangle = Triangle(name="ff", base=3, height=2, first_side=4, second_side=4)
print(triangle.get_area())
