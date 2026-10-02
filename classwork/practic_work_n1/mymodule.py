import math

PI = math.pi
VERSION = "1.0.0"

def circle_area(r):
    """Вычисляет площадь круга."""
    return PI * (r ** 2)

def circle_len(r):
    """Вычисляет длину окружности."""
    return 2 * PI * r

def _helper():
    """Закрытая функция по соглашению."""
    return PI / 2
