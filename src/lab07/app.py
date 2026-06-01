"""Бизнес-логика приложения. Слой между CLI и коллекцией."""

from typing import List, Optional, Callable, Any
from models import Weapon
from collection import Inventory
from base import Firearms, Edged
from exceptions import ItemNotFoundError, DuplicateItemError


class WeaponApp:
    """Основной класс приложения для работы с коллекцией оружия."""

    def __init__(self, inventory: Inventory):
        self._inventory = inventory

    def add_weapon(self, weapon: Weapon) -> None:
        """
        Добавить оружие в коллекцию.

        Raises:
            DuplicateItemError: если оружие с таким именем уже существует
        """
        try:
            self._inventory.add(weapon)
        except TypeError as e:
            raise DuplicateItemError(str(e))

    def remove_weapon(self, name: str) -> Weapon:
        """
        Удалить оружие по имени.

        Raises:
            ItemNotFoundError: если оружие не найдено
        """
        for i, weapon in enumerate(self._inventory._items):
            if weapon._imia == name:
                removed = self._inventory._items.pop(i)
                return removed
        raise ItemNotFoundError(f"Оружие '{name}' не найдено в коллекции.")

    def find_by_name(self, name: str) -> Optional[Weapon]:
        """Найти оружие по имени."""
        return self._inventory.find_by_imia(name)

    def get_all_weapons(self) -> List[Weapon]:
        """Получить все оружие из коллекции."""
        return self._inventory._items.copy()

    def sort_by_strategy(self, strategy: Callable[[Weapon], Any]) -> List[Weapon]:
        """Отсортировать коллекцию по стратегии."""
        self._inventory._items.sort(key=strategy)
        return self._inventory._items

    def filter_by_predicate(self, predicate: Callable[[Weapon], bool]) -> List[Weapon]:
        """Отфильтровать оружие по предикату."""
        return [w for w in self._inventory._items if predicate(w)]

    def filter_by_type(self, weapon_type: str) -> List[Weapon]:
        """Отфильтровать оружие по типу ('Firearms', 'Edged', 'Weapon')."""
        if weapon_type == 'Firearms':
            return [w for w in self._inventory._items if isinstance(w, Firearms)]
        elif weapon_type == 'Edged':
            return [w for w in self._inventory._items if isinstance(w, Edged)]
        else:
            return [w for w in self._inventory._items if isinstance(w, Weapon)]

    def get_broken_weapons(self) -> List[Weapon]:
        """Получить сломанное оружие (прочность = 0)."""
        return [w for w in self._inventory._items if w._hardness == 0]

    def repair_weapon(self, name: str) -> str:
        """
        Починить оружие по имени.

        Raises:
            ItemNotFoundError: если оружие не найдено
        """
        weapon = self.find_by_name(name)
        if weapon is None:
            raise ItemNotFoundError(f"Оружие '{name}' не найдено.")
        return weapon.repair()

    def upgrade_weapon(self, name: str, upgrade_strategy: Any) -> str:
        """
        Применить стратегию улучшения к оружию.

        Raises:
            ItemNotFoundError: если оружие не найдено
        """
        weapon = self.find_by_name(name)
        if weapon is None:
            raise ItemNotFoundError(f"Оружие '{name}' не найдено.")
        return upgrade_strategy(weapon)

    def count(self) -> int:
        """Вернуть количество оружия в коллекции."""
        return len(self._inventory._items)

    # --- Фабричные методы для создания оружия (перенесено из CLI) ---

    def create_weapon(self, damage: int, rare: str, hardness: int, effects: str,
                      tip: str, imia: str, kolichestvo: int) -> Weapon:
        """Создать базовое оружие."""
        return Weapon(damage, rare, hardness, effects, tip, imia, kolichestvo)

    def create_firearms(self, damage: int, rare: str, hardness: int, effects: str,
                        tip: str, imia: str, kolichestvo: int,
                        caliber: float, magazine_capacity: int) -> Firearms:
        """Создать огнестрельное оружие."""
        return Firearms(damage, rare, hardness, effects, tip, imia, kolichestvo,
                        caliber, magazine_capacity)

    def create_edged(self, damage: int, rare: str, hardness: int, effects: str,
                     tip: str, imia: str, kolichestvo: int,
                     blade_length: float, material: str) -> Edged:
        """Создать холодное оружие."""
        return Edged(damage, rare, hardness, effects, tip, imia, kolichestvo,
                     blade_length, material)
