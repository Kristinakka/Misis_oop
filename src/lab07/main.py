"""Точка входа в приложение."""

import os
from collection import Inventory
from app import WeaponApp
from cli import CLI
from storage import load, save

DATA_FILE = "weapons.json"


def main() -> None:
    print("ИНВЕНТАРЬ ОРУЖИЯ")
    print("Загрузка данных...")

    inventory = load(DATA_FILE)
    app = WeaponApp(inventory)
    cli = CLI(app)

    try:
        cli.run()
    except KeyboardInterrupt:
        print("\nПрерывание пользователя")
    finally:
        save(inventory, DATA_FILE)
        print(f"Данные сохранены в {DATA_FILE}")


if __name__ == "__main__":
    main()
