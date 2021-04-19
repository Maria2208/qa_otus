from source.Figure import Circle
from math import pi
import pytest


def test_check_area(default_circle):
    """Метод проверяет площадь переданного круга"""
    assert default_circle.get_area() == pi * default_circle.radius ** 2


def test_check_perimeter(default_circle):
    """Метод проверяет периметр переданного круга"""
    assert default_circle.get_perimeter() == 2 * pi * default_circle.radius


def test_circle_has_negative_radius():
    """Метод проверяет, что выбрасывается исключение, если в радиусе передать отрицательное значение"""
    with pytest.raises(ValueError):
        Circle(name="круг", radius=-1).check_values()


def test_circle_has_string_radius():
    """Метод проверяет, что выбрасывается исключение, если в радиусе передать строку"""
    with pytest.raises(ValueError):
        Circle(name="круг", radius='abc').check_values()
