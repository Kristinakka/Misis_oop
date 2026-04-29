import sys
sys.path.append(r'C:\Users\Krist\OneDrive\Рабочий стол\Misis_oop\src\lab01')
from models import Weapon


class Inventory:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add(self, w):     #создаю метод и проверяю на дубликат и поиск с одинаковым именем
        if isinstance(w, Weapon) and w not in self._items:
            for d in self._items:
                if d._imia != w._imia:
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
        for w in self._item:
            if w._imia == imia:
                return w
            
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    def __getitem__(self, index):
        return self._items[index]
    
    def remove_at_index(self, index):
        if index >= 0 and index < len(self._items) and isinstance(index, int): 
            self._items.pop(index)
            return f'Элемент {self._items[index]} успешно удален'
        else:
            raise ValueError('Неверно указанный индекс')
        
    def sort_by_imia(self):
        self._items = sorted(self._items, key = lambda x: x._imia)
        return self._items

    def get_broken(self):
        Broken_Inv = Inventory()
        for i in self._items:
            if i._hardness < 0:
                Broken_Inv.add(i)
        return Broken_Inv.items()
    
items = Inventory()

x = Weapon(
    damage=50, 
    rare="Легендарное",  
    hardness=100, 
    effects="огонь, лед", 
    tip="Меч",  
    imia="Экскалибур", 
    kolichestvo=1
)

weapon1 = Weapon(
        damage=50, 
        rare="Легендарное",  
        hardness=100, 
        effects="огонь, лед", 
        tip="Меч",  
        imia="ddfр", 
        kolichestvo=1
    )
items.add(x)
items.add(weapon1)
print(items.remove_at_index())
