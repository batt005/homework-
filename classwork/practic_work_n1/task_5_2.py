import sys

def main():
    print("=== РАЗДЕЛ 5.2. АНАЛИЗ ЗАВИСИМОСТЕЙ ===")
    
    try:
        import packaging
        print(f"[OK] Библиотека 'packaging' успешно импортирована.")
        print(f"Версия в текущем окружении: {packaging.__version__}")
    except ImportError:
        print("[INFO] Библиотека 'packaging' не установлена в данном окружении.")
        print("Для изоляции версий в проектах A и B используйте отдельные папки .venv.")

if __name__ == '__main__':
    main()
