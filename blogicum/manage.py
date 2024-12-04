"""
Утилита командной строки Django для выполнения административных задач.
"""
import os
import sys


def main():
    """Запуск административных задач."""
    # Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE на настройки проекта 'blogicum'.
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogicum.settings')
    try:
        # Импортируем функцию для выполнения команд Django из командной строки.
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Если Django не удалось импортировать, выбрасываем ошибку с пояснением.
        raise ImportError(
            "Не удалось импортировать Django. Убедитесь, что он установлен "
            "и доступен в переменной окружения PYTHONPATH. "
            "Вы забыли активировать виртуальное окружение?"
        ) from exc
    # Выполняем команду, переданную через командную строку.
    execute_from_command_line(sys.argv)


# Если файл выполняется как основной скрипт, запускаем функцию main().
if __name__ == '__main__':
    main()