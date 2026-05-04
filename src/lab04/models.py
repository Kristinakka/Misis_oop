from validate import *
from interfaces import Printable, Repairable, Comparable

class Weapon:
    def __init__(self, damage, rare, hardness, effects, tip, imia, kolichestvo):
        self._imia = validate_imia(imia) 
        self._damage = validate_damage(damage)
        self._tip = validate_tip(tip)
        self._effects = validate_effects(effects)
        self._rare = validate_rare(rare)
        self._hardness = validate_hardness(hardness)
        self.__kolichestvo = validate_kolichestvo(kolichestvo)

    @property
    def imia(self):
        return self._imia
    
    @imia.setter
    def rename(self, new_name):
        if isinstance(new_name, str) and new_name != '':
            self._imia = new_name
        else:
            raise TypeError('Неверный формат названия оружия.')

    @property
    def status(self):
        if self._hardness > 0:
            return 'Состояние: Не сломано'
        else:
            return 'Состояние: Сломано'

    def __str__(self):
        if self._hardness > 0:
            return f'Вот краткая информация по вашему оружию! Название: {self._imia}, тип: {self._tip}, эффекты: {self._effects}, редкость: {self._rare}, урон: {self._damage}'
        else:
            return f'Ваше оружие сломано! Вот его характеристики: Название: {self._imia}, тип: {self._tip}, эффекты: {self._effects}, редкость: {self._rare}, урон: {self._damage}'

    def attack(self):
        if self._hardness == 0:
            return 'Ваше оружие сломано и не наносит урон противнику.'
        else:
            self._hardness -= 1
            return f'Вы попали по противнику и нанесли {self._damage} урона.' 

    def __repr__(self):
        return f'Вся информация по экземпляру. Название: {self._imia}, тип: {self._tip}, эффекты: {self._effects}, твердость: {self._hardness}, редкость: {self._rare}, урон: {self._damage}, количество пользователей: {self.__kolichestvo}'

    def __eq__(self, other):
        if isinstance(other, Weapon):
            return self._tip == other._tip
        return False
    
    def repair(self):
        if self._hardness < 100:
            self._hardness = 100
            return "Оружие восстановлено!"
        else:
            return "Ваше оружие имеет максимальную прочность!"


# классы с интерфейсами
class Firearms(Weapon, Printable, Repairable, Comparable):
    def __init__(self, damage, rare, hardness, effects, tip, imia, kolichestvo,
                 caliber, magazine_capacity):
        super().__init__(damage, rare, hardness, effects, tip, imia, kolichestvo)
        self._caliber = caliber         
        self._magazine_capacity = magazine_capacity  

    def reload(self):
        return f"Перезарядка! Магазин на {self._magazine_capacity} патронов."

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str}, Калибр: {self._caliber}, Магазин: {self._magazine_capacity}'

    def calculate_price(self):
        base_price = self._damage * 10
        if self._rare == 'легендарное':
            base_price *= 3
        elif self._rare == 'редкое':
            base_price *= 2
        return base_price + (self._caliber * 50) + (self._magazine_capacity * 10)

    # Реализация Printable
    def get_info(self) -> str:
        return f"{self._imia}, {self._caliber}мм, {self._magazine_capacity} патр, урон: {self._damage}"

    # Реализация Repairable
    def repair_weapon(self) -> str:
        if self._hardness < 100:
            self._hardness = 100
            return f"{self._imia} отремонтировано."
        return f"{self._imia} уже исправно."

    # Реализация Comparable
    def compare_to(self, other) -> int:
        if not isinstance(other, Weapon):
            raise TypeError("Можно сравнивать только оружие")
        if self._damage < other._damage:
            return -1
        elif self._damage == other._damage:
            return 0
        else:
            return 1


class Edged(Weapon, Printable, Repairable, Comparable):
    def __init__(self, damage, rare, hardness, effects, tip, imia, kolichestvo,
                 blade_length, material):
        super().__init__(damage, rare, hardness, effects, tip, imia, kolichestvo)
        self._blade_length = blade_length  
        self._material = material         

    def sharpen(self):
        return f"Заточка {self._imia}. Острота восстановлена."

    def __str__(self):
        parent_str = super().__str__()
        return f'{parent_str}, Клинок: {self._blade_length}см, Материал: {self._material}'

    def calculate_price(self):
        base_price = self._damage * 10
        if self._rare == 'легендарное':
            base_price *= 3
        elif self._rare == 'редкое':
            base_price *= 2
        return base_price + (self._blade_length * 20)

    # Реализация Printable
    def get_info(self) -> str:
        return f"{self._imia}, {self._material}, {self._blade_length}см, урон: {self._damage}"

    # Реализация Repairable
    def repair_weapon(self) -> str:
        if self._hardness < 100:
            self._hardness = 100
            return f"{self._imia} восстановлено."
        return f"{self._imia} в идеале."

    # Реализация Comparable
    def compare_to(self, other) -> int:
        if not isinstance(other, Weapon):
            raise TypeError("Можно сравнивать только оружие")
        if self._damage < other._damage:
            return -1
        elif self._damage == other._damage:
            return 0
        else:
            return 1


# коллекшн
class Inventory:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add(self, w):
        if isinstance(w, Weapon) and w not in self._items:
            self._items.append(w)
        else:
            raise TypeError('Неверный формат экземпляра.')
        
    def remove(self, w):
        if w in self._items:
            self._items.remove(w)
        else:
            raise TypeError('Элемента нет в списке')
            
    def get_all(self):
        return f'Вот ваш инвентарь:\n{self._items}'
        
    def find_by_imia(self, imia):
        for w in self._items:
            if w._imia == imia:
                return w
            
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def remove_at_index(self, index):
        if 0 <= index < len(self._items):
            self._items.pop(index)
            return f'Элемент успешно удален'
        else:
            raise ValueError('Неверно указанный индекс')
        
    def sort_by_imia(self):
        self._items = sorted(self._items, key=lambda x: x._imia)
        return self._items

    def get_broken(self):
        Broken_Inv = Inventory()
        for i in self._items:
            if i._hardness <= 0:
                Broken_Inv.add(i)
        return Broken_Inv
    
    # нью методы
    
    def get_printable_items(self): # фильтрация по Printable ну пон
        new_inv = Inventory()
        for item in self._items:
            if isinstance(item, Printable):
                new_inv.add(item)
        return new_inv
    
    def get_repairable_items(self):             # фильтрация по интерфейсу Repairable
        new_inv = Inventory()
        for item in self._items:
            if isinstance(item, Repairable):
                new_inv.add(item)
        return new_inv
    
    def get_comparable_items(self):         # фильтрация по интерфейсу Comparable
        new_inv = Inventory()
        for item in self._items:
            if isinstance(item, Comparable):
                new_inv.add(item)
        return new_inv
    
    def print_all_info(self):       # вывод информации через интерфейс Printable
        for item in self._items:
            if isinstance(item, Printable):
                print(f"  {item.get_info()}")
    
    def sort_by_damage(self):               # сортировка через интерфейс Comparable
        comparable_items = [item for item in self._items if isinstance(item, Comparable)]
        non_comparable = [item for item in self._items if not isinstance(item, Comparable)]
        
        # Сортировка пузырьком через compare_to
        for i in range(len(comparable_items)):
            for j in range(i + 1, len(comparable_items)):
                if comparable_items[i].compare_to(comparable_items[j]) > 0:
                    comparable_items[i], comparable_items[j] = comparable_items[j], comparable_items[i]
        
        self._items = comparable_items + non_comparable
        return self._items