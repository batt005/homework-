price = float(input("Введите цену за 1 кг конфет: "))
for kg in range(1, 11):
    cost = kg * price
    print(f"Стоимость {kg} кг конфет: {cost}")
