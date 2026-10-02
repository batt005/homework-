import sched
import time
import random
import math

def format_time():
    """Возвращает текущее системное время для логов."""
    return time.strftime("%H:%M:%S")

def generate_telemetry(step):
    """Генерирует случайные, но математически обоснованные параметры корабля."""
    # Синусоидальное изменение температуры с небольшой случайной флуктуацией
    base_temp = 40.0 + 10.0 * math.sin(step * 0.5)
    temperature = base_temp + random.uniform(-1.5, 1.5)
    
    # Заряд батареи линейно падает, но не опускается ниже 0
    battery = max(0.0, 100.0 - (step * 2.5) + random.uniform(-0.5, 0.5))
    
    # Статус систем выбирается случайно из списка с весами (шансами)
    statuses = ['OK', 'WARNING', 'CRITICAL']
    system_status = random.choices(statuses, weights=[85, 12, 3], k=1)[0]
    
    return temperature, battery, system_status

def telemetry_event(scheduler, step, max_steps):
    """Функция одного шага сбора телеметрии, которая планирует саму себя."""
    temp, batt, status = generate_telemetry(step)
    
    print(f"[{format_time()}] [ШАГ {step}/{max_steps}] "
          f"Термо: {temp:.2f}°C | Батарея: {batt:.1f}% | Статус: {status}")
    
    # Если шаг не последний, планируем следующий через 1 секунду
    if step < max_steps:
        scheduler.enter(1.0, 1, telemetry_event, (scheduler, step + 1, max_steps))
    else:
        print(f"[{format_time()}] Сбор телеметрии успешно завершен.")

def main():
    print(f"[{format_time()}] === ЗАПУСК МИССИИ 'АРЕС-1' ===")
    
    # Фиксируем seed для воспроизводимости тестов, как требует методичка
    random.seed(101)
    
    # Инициализируем планировщик sched
    mission_control = sched.scheduler(time.time, time.sleep)
    
    total_steps = 10
    print(f"Запланирован мониторинг на {total_steps} шагов с интервалом в 1 сек.")
    
    # Планируем самое первое событие телеметрии (старт на шаге 1)
    mission_control.enter(0.0, 1, telemetry_event, (mission_control, 1, total_steps))
    
    # Запуск планировщика (блокирует поток до конца миссии)
    mission_control.run()
    
    print(f"[{format_time()}] === МИССИЯ 'АРЕС-1' БЛАГОПОЛУЧНО ЗАВЕРШЕНА ===")

if __name__ == '__main__':
    main()
