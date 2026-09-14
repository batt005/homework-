price = float(input("Введите цену за 1 кг конфет: "))
weight = 1.2
while weight <= 2.01:
    cost = weight * price
    print(f"Стоимость {weight:.1f} кг: {cost:.2f}")
    weight += 0.2
