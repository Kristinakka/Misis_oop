"""Консольный интерфейс пользователя (CLI). Только ввод/вывод."""

from typing import List, Optional
from models import Weapon
from collection import Inventory
from base import Firearms, Edged
from app import WeaponApp
from exceptions import ItemNotFoundError, DuplicateItemError
from strategies import (
    by_name, by_damage, by_rarity, by_damage_then_name, by_price,
    is_legendary, is_high_damage, is_repairable, is_firearms, is_edged,
    make_damage_filter, make_rarity_filter,
    DamageUpgradeStrategy, RarityUpgradeStrategy, RepairStrategy
)


class CLI:
    """Класс для управления консольным интерфейсом."""
    
    def __init__(self, app: WeaponApp):
        """
        Инициализация CLI.
        
        Args:
            app: объект бизнес-логики WeaponApp
        """
        self._app = app
    
    def _display_menu(self) -> None:
        """Показать главное меню."""
        print("                     ИНВЕНТАРЬ ОРУЖИЯ")
        print("1.Добавить оружие")
        print("2.Показать всё оружие")
        print("3.Найти оружие по названию")
        print("4.Удалить оружие")
        print("5.Сортировка (стратегии)")
        print("6.Фильтрация")
        print("7.Показать сломанное оружие")
        print("8.Почнить оружие")
        print("9.Улучшить оружие")
        print("0.Выход и сохранение")
    
    
    def _display_weapons_table(self, weapons: List[Weapon], title: str = "Оружие") -> None:
        """Отобразить список оружия в виде таблицы."""
        if not weapons:
            print(f"\n{title}: пусто")
            return
        
        print(f"\n{title} (всего: {len(weapons)}):")
        print(f"{'Название':<22} {'Тип':<14} {'Урон':<8} {'Прочность':<10} {'Редкость':<16} {'Инфо'}")
      
        
        for w in weapons:
            if isinstance(w, Firearms):
                w_type = "Огнестрельное"
                extra_info = f"{w._caliber}мм/{w._magazine_capacity}"
            elif isinstance(w, Edged):
                w_type = "Холодное"
                extra_info = f"{w._blade_length}см/{w._material}"
            else:
                w_type = "Обычное"
                extra_info = "-"
            
            # Индикатор сломанности
            status = "noob" if w._hardness == 0 else "pro"
            
            print(f"{status} {w._imia:<20} {w_type:<14} {w._damage:<8} {w._hardness:<10} {w._rare:<16} {extra_info}")
        
    
    def _add_weapon(self) -> None:
        """Диалог добавления нового оружия."""
        print("\n--- Добавление оружия ---")
        print("Тип оружия:")
        print("1. Обычное оружие (Weapon)")
        print("2. Огнестрельное (Firearms)")
        print("3. Холодное (Edged)")
        
        try:
            choice = int(input("Выберите тип (1-3): "))
            if choice not in [1, 2, 3]:
                print("Ошибка: выберите 1, 2 или 3")
                return
        except ValueError:
            print("Ошибка: введите число")
            return
        
        try:
            imia = input("Название: ").strip()
            if not imia:
                print("Ошибка: название не может быть пустым")
                return
            
            damage = int(input("Урон (целое число >0): "))
            rare = input("Редкость (Обычное/Редкое/Сверхредкое/Эпическое/Мифическое/Легендарное): ").strip()
            hardness = int(input("Прочность (0-100): "))
            effects = input("Эффекты: ").strip()
            tip = input("Тип (Нож/Дубинка/Меч/Топор/Копье/Лук/Арбалет/Кувалда/Щит/Пушка): ").strip()
            kolichestvo = int(input("Количество обладателей: "))
            
            if choice == 1:
                weapon = Weapon(damage, rare, hardness, effects, tip, imia, kolichestvo)
            elif choice == 2:
                caliber = float(input("Калибр (мм): "))
                magazine_capacity = int(input("Ёмкость магазина: "))
                weapon = Firearms(damage, rare, hardness, effects, tip, imia, 
                                 kolichestvo, caliber, magazine_capacity)
            else:
                blade_length = float(input("Длина клинка (см): "))
                material = input("Материал: ").strip()
                weapon = Edged(damage, rare, hardness, effects, tip, imia,
                              kolichestvo, blade_length, material)
            
            self._app.add_weapon(weapon)
            print(f"\n Оружие '{imia}' успешно добавлено!")
            
            # Показываем информацию через интерфейсы если есть
            if hasattr(weapon, 'get_info'):
                print(f" {weapon.get_info()}")
            
        except DuplicateItemError as e:
            print(f"\nОшибка: {e}")
        except (ValueError, TypeError) as e:
            print(f"\nОшибка ввода: {e}")
    
    def _show_all(self) -> None:
        """Показать всё оружие."""
        weapons = self._app.get_all_weapons()
        self._display_weapons_table(weapons, "ВСЁ ОРУЖИЕ")
        
        # Демонстрация Printable интерфейса
        print("\nДетальная информация (Printable):")
        for w in weapons:
            if hasattr(w, 'get_info'):
                print(f"   • {w.get_info()}")
    
    def _find_weapon(self) -> None:
        """Найти оружие по имени."""
        name = input("\nВведите название оружия для поиска: ").strip()
        if not name:
            print("Ошибка: название не может быть пустым")
            return
        
        weapon = self._app.find_by_name(name)
        if weapon:
            print(f"\nНайдено:")
            print(f"   {weapon}")
            if hasattr(weapon, 'get_info'):
                print(f"{weapon.get_info()}")
            if hasattr(weapon, 'calculate_price'):
                print(f"Цена: {weapon.calculate_price()}")
        else:
            print(f"\nОружие '{name}' не найдено")
            raise ItemNotFoundError(f"Оружие '{name}' не найдено")  # Демонстрация исключения
    
    def _remove_weapon(self) -> None:
        """Удалить оружие с подтверждением."""
        name = input("\nВведите название оружия для удаления: ").strip()
        if not name:
            print("Ошибка: название не может быть пустым")
            return
        
        weapon = self._app.find_by_name(name)
        if not weapon:
            print(f"\nОружие '{name}' не найдено")
            return
        
        # Подтверждение опасной операции
        print(f"\nОружие: {weapon}")
        confirm = input(f"Удалить '{name}'? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Удаление отменено")
            return
        
        try:
            removed = self._app.remove_weapon(name)
            print(f"\nОружие '{removed._imia}' удалено!")
        except ItemNotFoundError as e:
            print(f"\n{e}")
    
    def _sort_menu(self) -> None:
        """Меню сортировки с выбором стратегии."""
        print("\n--- Сортировка (паттерн Стратегия) ---")
        print("1. По имени (by_name)")
        print("2. По урону (by_damage)")
        print("3. По редкости (by_rarity)")
        print("4. По урону → имени (by_damage_then_name)")
        print("5. По цене (by_price)")
        
        try:
            choice = int(input("Выберите стратегию (1-5): "))
        except ValueError:
            print("Ошибка: введите число")
            return
        
        strategy_map = {
            1: by_name,
            2: by_damage,
            3: by_rarity,
            4: by_damage_then_name,
            5: by_price
        }
        
        if choice not in strategy_map:
            print("Неверный пункт")
            return
        
        strategy = strategy_map[choice]
        weapons = self._app.sort_by_strategy(strategy)
        strategy_name = ["", "по имени", "по урону", "по редкости", "по урону+имени", "по цене"][choice]
        self._display_weapons_table(weapons, f"ОТСОРТИРОВАНО ({strategy_name})")
    
    def _filter_menu(self) -> None:
        """Меню фильтрации."""
        print("\n--- Фильтрация ---")
        print("1. Только легендарное оружие")
        print("2. Только с высоким уроном (>=100)")
        print("3. Требует ремонта (прочность < 100)")
        print("4. Только огнестрельное")
        print("5. Только холодное оружие")
        print("6. Фильтр по диапазону урона (фабрика)")
        print("7. Фильтр по редкости (фабрика)")
        
        try:
            choice = int(input("Выберите фильтр (1-7): "))
        except ValueError:
            print("Ошибка: введите число")
            return
        
        filters = {
            1: is_legendary,
            2: lambda w: is_high_damage(w, 100),
            3: is_repairable,
            4: is_firearms,
            5: is_edged
        }
        
        if choice in filters:
            filtered = self._app.filter_by_predicate(filters[choice])
            filter_names = ["", "легендарное", "высокий урон", "требует ремонта", 
                           "огнестрельное", "холодное"][choice]
            self._display_weapons_table(filtered, f"ФИЛЬТР: {filter_names}")
        
        elif choice == 6:
            try:
                min_damage = int(input("Минимальный урон: "))
                max_input = input("Максимальный урон (Enter для без上限): ").strip()
                max_damage = int(max_input) if max_input else None
                filter_fn = make_damage_filter(min_damage, max_damage)
                filtered = self._app.filter_by_predicate(filter_fn)
                range_str = f"{min_damage}" + (f"-{max_damage}" if max_damage else "+")
                self._display_weapons_table(filtered, f"ФИЛЬТР: урон {range_str}")
            except ValueError:
                print("Ошибка: введите корректные числа")
        
        elif choice == 7:
            rare = input("Редкость (обычное/редкое/легендарное): ").strip().lower()
            if rare in ['обычное', 'редкое', 'легендарное']:
                filter_fn = make_rarity_filter(rare)
                filtered = self._app.filter_by_predicate(filter_fn)
                self._display_weapons_table(filtered, f"ФИЛЬТР: редкость={rare}")
            else:
                print("Неверная редкость")
        
        else:
            print("Неверный пункт")
    
    def _show_broken(self) -> None:
        """Показать сломанное оружие."""
        broken = self._app.get_broken_weapons()
        self._display_weapons_table(broken, "СЛОМАННОЕ ОРУЖИЕ")
    
    def _repair_weapon(self) -> None:
        """Починить оружие."""
        name = input("\nВведите название оружия для ремонта: ").strip()
        if not name:
            print("Ошибка: название не может быть пустым")
            return
        
        try:
            result = self._app.repair_weapon(name)
            print(f"\n{result}")
            
            # Показываем обновлённое состояние
            weapon = self._app.find_by_name(name)
            if weapon:
                print(f"Текущая прочность: {weapon._hardness}")
        except ItemNotFoundError as e:
            print(f"\n{e}")
    
    def _upgrade_menu(self) -> None:
        """Меню улучшения оружия."""
        name = input("\nВведите название оружия для улучшения: ").strip()
        if not name:
            print("Ошибка: название не может быть пустым")
            return
        
        print("\n--- Стратегии улучшения ---")
        print("1. Повысить урон (+50)")
        print("2. Повысить редкость")
        print("3. Полный ремонт")
        
        try:
            choice = int(input("Выберите стратегию (1-3): "))
        except ValueError:
            print("Ошибка: введите число")
            return
        
        strategies = {
            1: DamageUpgradeStrategy(50),
            2: RarityUpgradeStrategy(),
            3: RepairStrategy()
        }
        
        if choice not in strategies:
            print("Неверный пункт")
            return
        
        try:
            result = self._app.upgrade_weapon(name, strategies[choice])
            print(f"\n{result}")
        except ItemNotFoundError as e:
            print(f"\n{e}")
    
    def run(self) -> None:
        """Запуск главного цикла CLI."""
        menu_actions = {
            1: self._add_weapon,
            2: self._show_all,
            3: self._find_weapon,
            4: self._remove_weapon,
            5: self._sort_menu,
            6: self._filter_menu,
            7: self._show_broken,
            8: self._repair_weapon,
            9: self._upgrade_menu,
        }
        
        while True:
            self._display_menu()
            
            try:
                choice = int(input("Выберите пункт: "))
            except ValueError:
                print(" Ошибка: введите число (0-9)")
                continue
            
            if choice == 0:
                print("\nДо свидания!")
                break
            
            if choice in menu_actions:
                menu_actions[choice]()
            else:
                print("\nНеверный пункт меню. Выберите 0-9.")