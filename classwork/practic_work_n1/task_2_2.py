import random
import math

def main():
    # 1. Собираем колоду из 36 карт генератором списка
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    deck = [f"{r}{s}" for s in suits for r in ranks]
    print(f"Всего карт в колоде: {len(deck)}")

    # 2. Раздаем «руку» из 5 карт через sample и «карту дня» через choice
    hand = random.sample(deck, 5)
    card_of_the_day = random.choice(deck)
    print(f"Рука игрока (sample): {hand}")
    print(f"Карта дня (choice) : {card_of_the_day}")

    # 3. Смоделируем выпадение лута с весами 70/25/5 через choices
    loot_pool = ['обычная', 'редкая', 'легендарная']
    loot_weights = [70, 25, 5]
    dropped_loot = random.choices(loot_pool, weights=loot_weights, k=5)
    print(f"Лут (choices, 5 шт.): {dropped_loot}")

    # 4. Перемешиваем колоду через shuffle и выводим первые 6 карт
    # ВНИМАНИЕ: shuffle меняет список НА МЕСТЕ, поэтому делаем копию
    shuffled_deck = deck.copy()
    random.shuffle(shuffled_deck)
    print(f"После shuffle : {shuffled_deck[:6]} ...")

    # 5. Честная раздача по 5 карт трем игрокам (карты не должны повторяться)
    # Чтобы карты не дублировались, мы берем срез из уже перемешанной колоды
    print("\n--- Раздача 3 игрокам по 5 карт ---")
    print(f"Алиса : {shuffled_deck[0:5]}")
    print(f"Борис : {shuffled_deck[5:10]}")
    print(f"Вера  : {shuffled_deck[10:15]}")

if __name__ == '__main__':
    main()
