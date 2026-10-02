import sched
import time

def emergency_alert(message):
    print(f"[{time.strftime('%H:%M:%S')}] СИСТЕМА: {message}")

def main():
    s = sched.scheduler(time.time, time.sleep)
    print("=== РАЗДЕЛ 7.2. УПРАВЛЕНИЕ ОЧЕРЕДЬЮ И ОТМЕНА ЗАДАЧ ===")

    # Планируем три важных события
    e1 = s.enter(2.0, 1, emergency_alert, ("Проверка давления в норме",))
    e2 = s.enter(4.0, 1, emergency_alert, ("КРИТИЧЕСКИЙ СБОЙ: Утечка топлива!",))
    e3 = s.enter(6.0, 1, emergency_alert, ("Плановая калибровка датчиков",))

    print(f"Запланировано задач в очереди: {len(s.queue)}")

    # Симулируем работу диспетчера: обнаружили ложную тревогу и отменяем событие e2
    print("Диспетчер: Обнаружен ложный сигнал тревоги. Отмена задачи e2...")
    try:
        s.cancel(e2)
        print("[Успешно] Событие e2 удалено из очереди.")
    except ValueError:
        print("[Ошибка] Не удалось отменить событие.")

    print(f"Осталось задач в очереди перед запуском: {len(s.queue)}")
    print("Запуск планировщика...")
    s.run()
    print("Все оставшиеся задачи выполнены.")

if __name__ == '__main__':
    main()
