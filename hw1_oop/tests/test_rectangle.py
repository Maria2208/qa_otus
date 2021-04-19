import pytest
from hw1_oop.source.Figure import Rectangle


def test_check_area(default_rectangle):
    """Метод проверяет площадь переданного прямоугольника"""
    assert default_rectangle.get_area() == default_rectangle.length * default_rectangle.width


def test_check_perimeter(default_rectangle):
    """Метод проверяет периметр переданного прямоугольника"""
    assert default_rectangle.get_perimeter() == 2 * (default_rectangle.length + default_rectangle.width)


def test_rectangle_has_negative_length():
    """Метод проверяет, что выбрасывается исключение, если в length передать отрицательное значение"""
    with pytest.raises(ValueError):
        Rectangle(name="прямоугольник", length=-1, width=1).check_values()


def test_rectangle_has_string_length():
    """Метод проверяет, что выбрасывается исключение, если в length передать строковое значение"""
    with pytest.raises(ValueError):
        Rectangle(name="прямоугольник", length="абс", width=1).check_values()


def test_rectangle_has_negative_width():
    """Метод проверяет, что выбрасывается исключение, если в width передать отрицательное значение"""
    with pytest.raises(ValueError):
        Rectangle(name="прямоугольник", length=1, width=-1).check_values()


def test_rectangle_has_string_width():
    """Метод проверяет, что выбрасывается исключение, если в width передать строковое значение"""
    with pytest.raises(ValueError):
        Rectangle(name="прямоугольник", length=1, width='abc').check_values()
