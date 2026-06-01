from models import Weapon


class Inventory:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add(self, w):
        # Исправлен баг: оригинальный код добавлял элемент внутри цикла при каждом несовпадении имени.
        # Теперь: проверяем дубликат по имени один раз перед добавлением.
        if not isinstance(w, Weapon):
            raise TypeError('Неверный формат экземпляра.')
        if w in self._items:
            raise TypeError('Элемент уже существует в инвентаре.')
        for existing in self._items:
            if existing._imia == w._imia:
                raise TypeError(f"Оружие с именем '{w._imia}' уже существует.")
        self._items.append(w)

    def remove(self, w):
        if w in self._items:
            self._items.remove(w)
        else:
            raise TypeError('Элемента нет в списке')

    def get_all(self):
        return f'Вот ваш инвентарь:\n{self._items}'

    def find_by_imia(self, imia):
        # Исправлен баг: self._item -> self._items
        for w in self._items:
            if w._imia == imia:
                return w
        return None

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def remove_at_index(self, index):
        # Исправлен баг: оригинал обращался к self._items[index] после pop — индекс уже недействителен.
        if not isinstance(index, int) or index < 0 or index >= len(self._items):
            raise ValueError('Неверно указанный индекс')
        removed = self._items[index]
        self._items.pop(index)
        return f'Элемент {removed} успешно удален'

    def sort_by_imia(self):
        self._items = sorted(self._items, key=lambda x: x._imia)
        return self._items

    def get_broken(self):
        # Исправлен баг 1: условие было i._hardness < 0, сломанное оружие имеет hardness == 0.
        # Исправлен баг 2: Broken_Inv.items() — items это property, не метод.
        broken = Inventory()
        for i in self._items:
            if i._hardness == 0:
                broken.add(i)
        return broken.items
