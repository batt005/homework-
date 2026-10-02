import math

def calculate_orbit(step):
    """Рассчитывает высоту орбиты корабля по синусоидальной траектории."""
    base_altitude = 400.0  # Базовая высота МКС в км
    # Моделируем небольшие колебания высоты
    altitude = base_altitude + 20.0 * math.sin(step * 0.5)
    return altitude
