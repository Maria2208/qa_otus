import pytest
from source.Figure import Triangle


def test_check_area(default_triangle):
    """Метод проверяет площадь переданного треугольника"""
    assert default_triangle.get_area() == 0.5 * default_triangle.base * default_triangle.height


def test_check_perimeter(default_triangle):
    """Метод проверяет периметр переданного треугольника"""
    assert default_triangle.get_perimeter() == default_triangle.first_side + default_triangle.base + \
           + default_triangle.second_side


def test_square_has_negative_base():
    """Метод проверяет, что выбрасывается исключение, если в base передать отрицательное значение"""
    with pytest.raises(ValueError):
        Triangle(name="прямоугольник", base=-1, height=2, first_side=1, second_side=2)


def test_square_has_string_base():
    """Метод проверяет, что выбрасывается исключение, если в base передать строковое значение"""
    with pytest.raises(ValueError):
        Triangle(name="прямоугольник", base="abc", height=2, first_side=1, second_side=2)


def test_square_has_negative_height():
    """Метод проверяет, что выбрасывается исключение, если в height передать отрицательное значение"""
    with pytest.raises(ValueError):
        Triangle(name="прямоугольник", base=1, height=-2, first_side=1, second_side=2)


def test_square_has_string_height():
    """Метод проверяет, что выбрасывается исключение, если в height передать строковое значение"""
    with pytest.raises(ValueError):
        Triangle(name="прямоугольник", base=1, height="abc", first_side=1, second_side=2)


def test_square_has_negative_first_side():
    """Метод проверяет, что выбрасывается исключение, если в first_side передать отрицательное значение"""
    with pytest.raises(ValueError):
        Triangle(name="прямоугольник", base=1, height=2, first_side=-1, second_side=2)


def test_square_has_string_first_side():
    """Метод проверяет, что выбрасывается исключение, если в first_side передать строковое значение"""
    with pytest.raises(ValueError):
        Triangle(name="прямоугольник", base=1, height=1, first_side="abc", second_side=2)


def test_square_has_negative_second_side():
    """Метод проверяет, что выбрасывается исключение, если в second_side передать отрицательное значение"""
    with pytest.raises(ValueError):
        Triangle(name="прямоугольник", base=1, height=2, first_side=1, second_side=-2)


def test_square_has_string_second_side():
    """Метод проверяет, что выбрасывается исключение, если в second_side передать строковое значение"""
    with pytest.raises(ValueError):
        Triangle(name="прямоугольник", base=1, height=1, first_side=2, second_side="abc")
