import pytest
from source.Figure import Square


def test_check_area(default_square):
    """Метод проверяет площадь переданного квадрата"""
    assert default_square.get_area() == default_square.side_length ** 2


def test_check_perimeter(default_square):
    """Метод проверяет периметр переданного квадрата"""
    assert default_square.get_perimeter() == default_square.side_length * 4


def test_square_has_negative_side_length():
    """Метод проверяет, что выбрасывается исключение, если в side_length передать отрицательное значение"""
    with pytest.raises(ValueError):
        Square(name="прямоугольник", side_length=-1)


def test_square_has_string_side_length():
    """Метод проверяет, что выбрасывается исключение, если в side_length передать строковое значение"""
    with pytest.raises(ValueError):
        Square(name="прямоугольник", side_length="абс")