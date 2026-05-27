"""Бизнес-логика приложения. Слой между CLI и коллекцией."""

from typing import List, Optional, Callable, Any
from models import Weapon
from collection import Inventory
from base import Firearms, Edged
from exceptions import ItemNotFoundError, DuplicateItemError


class WeaponApp:
    """Основной класс приложения для работы с коллекцией оружия."""
    
    def __init__(self, inventory: Inventory):
        """
        Инициализация приложения.
        
        Args:
            inventory: объект Inventory с коллекцией оружия
        """
        self._inventory = inventory
    
    def _check_duplicate_by_name(self, name: str) -> bool:
        """Проверить, существует ли оружие с таким именем."""
        for weapon in self._inventory._items:
            if weapon._imia == name:
                return True
        return False
    
    def add_weapon(self, weapon: Weapon) -> None:
        """
        Добавить оружие в коллекцию.
        
        Args:
            weapon: объект Weapon
            
        Raises:
            DuplicateItemError: если оружие с таким именем уже существует
        """
        # Проверка на дубликат по имени (обходим баг в Inventory.add)
        if self._check_duplicate_by_name(weapon._imia):
            raise DuplicateItemError(
                f"Оружие с именем '{weapon._imia}' уже существует!"
            )
        
        # Обходим баг в Inventory.add() через прямой доступ
        if weapon not in self._inventory._items:
            self._inventory._items.append(weapon)
    
    def remove_weapon(self, name: str) -> Weapon:
        """
        Удалить оружие по имени.
        
        Args:
            name: название оружия для удаления
            
        Returns:
            Weapon: удалённое оружие
            
        Raises:
            ItemNotFoundError: если оружие не найдено
        """
        for i, weapon in enumerate(self._inventory._items):
            if weapon._imia == name:
                removed = self._inventory._items.pop(i)
                return removed
        raise ItemNotFoundError(f"Оружие '{name}' не найдено в коллекции.")
    
    def find_by_name(self, name: str) -> Optional[Weapon]:
        """
        Найти оружие по имени.
        
        Args:
            name: название оружия
            
        Returns:
            Optional[Weapon]: найденное оружие или None
        """
        for weapon in self._inventory._items:
            if weapon._imia == name:
                return weapon
        return None
    
    def get_all_weapons(self) -> List[Weapon]:
        """
        Получить все оружие из коллекции.
        
        Returns:
            List[Weapon]: список всего оружия
        """
        return self._inventory._items.copy()
    
    def sort_by_strategy(self, strategy: Callable[[Weapon], Any]) -> List[Weapon]:
        """
        Отсортировать коллекцию по стратегии.
        
        Args:
            strategy: функция-ключ для сортировки
            
        Returns:
            List[Weapon]: отсортированный список
        """
        self._inventory._items.sort(key=strategy)
        return self._inventory._items
    
    def filter_by_predicate(self, predicate: Callable[[Weapon], bool]) -> List[Weapon]:
        """
        Отфильтровать оружие по предикату.
        
        Args:
            predicate: функция-условие для фильтрации
            
        Returns:
            List[Weapon]: отфильтрованный список
        """
        return [w for w in self._inventory._items if predicate(w)]
    
    def filter_by_type(self, weapon_type: str) -> List[Weapon]:
        """
        Отфильтровать оружие по типу.
        
        Args:
            weapon_type: 'Firearms', 'Edged', или 'Weapon'
            
        Returns:
            List[Weapon]: отфильтрованный список
        """
        if weapon_type == 'Firearms':
            return [w for w in self._inventory._items if isinstance(w, Firearms)]
        elif weapon_type == 'Edged':
            return [w for w in self._inventory._items if isinstance(w, Edged)]
        else:
            return [w for w in self._inventory._items if isinstance(w, Weapon)]
    
    def get_broken_weapons(self) -> List[Weapon]:
        """
        Получить сломанное оружие (прочность = 0).
        
        Returns:
            List[Weapon]: список сломанного оружия
        """
        return [w for w in self._inventory._items if w._hardness == 0]
    
    def repair_weapon(self, name: str) -> str:
        """
        Починить оружие по имени.
        
        Args:
            name: название оружия
            
        Returns:
            str: результат ремонта
            
        Raises:
            ItemNotFoundError: если оружие не найдено
        """
        weapon = self.find_by_name(name)
        if weapon is None:
            raise ItemNotFoundError(f"Оружие '{name}' не найдено.")
        
        if hasattr(weapon, 'repair_weapon'):
            return weapon.repair_weapon()
        else:
            return weapon.repair()
    
    def upgrade_weapon(self, name: str, upgrade_strategy: Any) -> str:
        """
        Применить стратегию улучшения к оружию.
        
        Args:
            name: название оружия
            upgrade_strategy: объект стратегии улучшения
            
        Returns:
            str: результат улучшения
            
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