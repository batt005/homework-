import sched
import time
import random
from mission.events import TelemetryTracker

def main():
    print(f"[{time.strftime('%H:%M:%S')}] === ЗАПУСК КОМПЛЕКСА ТЕЛЕМЕТРИИ АРЕС-1 ===")
    
    # Фиксируем seed для стабильности тестов
    random.seed(42)
    
    # Инициализируем планировщик задач
    sc = sched.scheduler(time.time, time.sleep)
    
    total_steps = 8
    tracker = TelemetryTracker(sc, total_steps)
    
    # Добавляем первое событие в очередь без задержки
    sc.enter(0.0, 1, tracker.track_step, (1,))
    
    # Запускаем планировщик миссии
    sc.run()
    
    print(f"[{time.strftime('%H:%M:%S')}] === ПРОГРАММА АРЕС-1 СДАЛА ОТЧЕТ И ЗАВЕРШИЛАСЬ ===")

if __name__ == '__main__':
    main()
