import sys
import os

def main():
    print("=== РАЗДЕЛ 4. ИНСПЕКЦИЯ ПАКЕТОВ (pip) ===")
    print(f"Версия Python: {sys.version.split()[0]}")
    
    # Ищем пути, куда pip складывает библиотеки
    site_packages = [p for p in sys.path if 'site-packages' in p]
    
    print("\nПути к site-packages в текущем окружении:")
    if site_packages:
        for path in site_packages:
            print(f" -> {path}")
    else:
        print(" -> site-packages не найден в путях sys.path!")
        
    print(f"\nТекущая рабочая директория скрипта:\n {os.getcwd()}")

if __name__ == '__main__':
    main()
