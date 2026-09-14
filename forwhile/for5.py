price = float(input("Введите цену за 1 кг конфет: "))
for kg in range(1, 11):
    weight = kg / 10
    cost = weight * price
    print(f"Стоимость {weight:.1f} кг конфет: {cost:.2f}")
