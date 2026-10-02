import sys
import site

def main():
    print("=== РАЗДЕЛ 5. ПРОВЕРКА ВИРТУАЛЬНОГО ОКРУЖЕНИЯ ===")
    print("Исполняемый файл:", sys.executable)
    print("Префикс         :", sys.prefix)
    print("Базовый префикс :", sys.base_prefix)
    print("В виртуальном окружении?", sys.prefix != sys.base_prefix)
    print("site-packages   :", site.getsitepackages())

if __name__ == '__main__':
    main()
