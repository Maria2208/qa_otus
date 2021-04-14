import pytest
from source.Figure import Triangle, Circle, Rectangle, Square


@pytest.fixture()
def default_triangle():
    triangle = Triangle(name="треугольник", base=3, height=4, first_side=2, second_side=2)
    yield triangle
    del triangle


@pytest.fixture()
def default_circle():
    circle = Circle(name="круг", radius=4)
    yield circle
    del circle


@pytest.fixture()
def default_rectangle():
    rectangle = Rectangle(name="прямоугольник", length=4, width=2)
    yield rectangle
    del rectangle


@pytest.fixture()
def default_square():
    square = Square(name="круг", side_length=4)
    yield square
    del square
