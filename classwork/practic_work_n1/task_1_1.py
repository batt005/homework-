import sys
import math
import random

def main():
    print(f"Версия Python: {sys.version.split()[0]}")
    print(f"Интерпретатор: {sys.executable}")
    print(f"Количество путей поиска: {len(sys.path)}")
    
    print("\nПервые 4 пути поиска:")
    for path in sys.path[:4]:
        print(f"    {path}")
        
    print("\n=== Математика и случайность ===")
    print(f"math.pi = {math.pi}")
    print(f"random.random() = {random.random()}")
    
    print("\n=== Загруженные модули ===")
    print(f"Всего загружено модулей: {len(sys.modules)}")
    print(f"Пример (первые 5): {sorted(list(sys.modules.keys()))[:5]}")
    
    public_math_names = [name for name in dir(math) if not name.startswith('_')]
    print(f"\nПубличных имён в math: {len(public_math_names)}")
    print(f"Первые 8: {public_math_names[:8]}")
    
    print(f"\nМой __name__ = {__name__}")

if __name__ == '__main__':
    main()
