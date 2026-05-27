"""Точка входа в приложение."""

import os
from collection import Inventory
from app import WeaponApp
from cli import CLI
from storage import load, save

DATA_FILE = "weapons.json"


def main() -> None:
    """Главная функция приложения."""
    print("ИНВЕНТАРЬ ОРУЖИЯ")
    print("Загрузка данных...")
    
    # Автоматическая загрузка данных при запуске
    inventory = load(DATA_FILE)
    
    # Создание приложения и CLI
    app = WeaponApp(inventory)
    cli = CLI(app)
    
    # Запуск интерактивного режима
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\nПрерывание пользователя")
    finally:
        # Автоматическое сохранение при выходе
        save(inventory, DATA_FILE)
        print(f"Данные сохранены в {DATA_FILE}")


if __name__ == "__main__":
    main()