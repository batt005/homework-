import math
from .flat import circle_area

def sphere_volume(r):
    """Вычисляет объем шара."""
    return (4/3) * math.pi * (r ** 3)

def cube_volume(a):
    """Вычисляет объем куба."""
    return a ** 3

def hemisphere_area(r):
    """Вычисляет площадь полусферы с использованием функции из flat.py."""
    return 3 * circle_area(r)
