from source.Figure import Rectangle, Circle, Triangle, Square


def test_add_area(default_triangle, default_square):
    """Метод проверяет сумму площадей двух фигур"""
    assert default_square.add_area(default_triangle) == default_triangle.get_area() + default_square.get_area()