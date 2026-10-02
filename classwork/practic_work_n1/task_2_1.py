import random

def main():
    # 1. Фиксируем начальное состояние для воспроизводимости
    random.seed(42)
    print("=== Базовые случайные числа ===")
    print(f"random()            : {random.random():.6f}")
    print(f"uniform(1, 10)      : {random.uniform(1, 10):.3f}")
    print(f"randint(1, 6)       : {random.randint(1, 6)}")
    print(f"randrange(0,100,5)  : {random.randrange(0, 100, 5)}")

    # 2. Моделируем 5 бросков двух игральных кубиков
    print("\n--- Бросок двух кубиков, 5 раз ---")
    for i in range(1, 6):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        print(f"Бросок {i}: {d1} + {d2} = {d1 + d2}")

    # 3. 10 000 бросков одного кубика для сбора статистики
    print("\n--- Статистика 10000 бросков одного кубика ---")
    stats = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    
    for _ in range(10000):
        face = random.randint(1, 6)
        stats[face] += 1
        
    # 4. Выводим результаты и строим текстовую гистограмму
    for face, count in stats.items():
        percentage = (count / 10000) * 100
        # Один символ '#' на каждые 50 выпадений
        bar = "#" * (count // 50)
        print(f"{face}: {count:4d} ({percentage:5.2f}%) {bar}")

if __name__ == '__main__':
    main()
