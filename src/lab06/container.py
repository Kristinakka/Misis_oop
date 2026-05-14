from typing import TypeVar, Generic, Callable, Optional, List, Protocol, Any, Iterator
from abc import ABC, abstractmethod


class Displayable(Protocol):        #Протокол для объектов, которые можно отобразить
    def display(self) -> str:       #Возвращает строковое представление объекта
        ...


class Scorable(Protocol):       #Протокол для объектов, которые имеют оценку/рейтинг
    def score(self) -> float:       #Возвращает числовую оценку объекта
        ...


#TypeVar с ограничениями

D = TypeVar('D', bound=Displayable)   # Тип с протоколом Displayable
S = TypeVar('S', bound=Scorable)      # Тип с протоколом Scorable
T = TypeVar('T')                      # Общий тип (без ограничений)
R = TypeVar('R')                      # Тип результата для map


#Generic-коллекция

class TypedCollection(Generic[T]):      #Обобщённая типизированная коллекция. Может хранить элементы только одного типа T.
    
    def __init__(self) -> None:
        """Инициализация пустой коллекции"""
        self._items: List[T] = []
    
    def add(self, item: T) -> None:
        """Добавляет элемент в коллекцию."""
        if item not in self._items:
            self._items.append(item)
    
    def remove(self, item: T) -> None:
        """Удаляет элемент из коллекции."""
        if item in self._items:
            self._items.remove(item)
        else:
            raise ValueError('Элемента нет в коллекции')
    
    def get_all(self) -> List[T]:
        """Возвращает копию списка всех элементов."""
        return list(self._items)
    
    def size(self) -> int:
        """Возвращает количество элементов в коллекции."""
        return len(self._items)
    
    def is_empty(self) -> bool:
        """Проверяет, пуста ли коллекция."""
        return len(self._items) == 0
    
    def clear(self) -> None:
        """Очищает коллекцию"""
        self._items.clear()
    
    def contains(self, item: T) -> bool:
        """Проверяет наличие элемента в коллекции."""
        return item in self._items
    
    #Методы для задания на 4
    
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Находит первый элемент, удовлетворяющий условию."""
        for item in self._items:
            if predicate(item):
                return item
        return None
    
    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        """Возвращает список всех элементов, удовлетворяющих условию."""
        return [item for item in self._items if predicate(item)]
    
    def map(self, transform: Callable[[T], R]) -> List[R]:
        """Применяет функцию преобразования к каждому элементу."""
        return [transform(item) for item in self._items]
    
    #Методы для работы с индексами 
    
    def remove_at_index(self, index: int) -> T:
        """Удаляет элемент по индексу."""
        if 0 <= index < len(self._items):
            return self._items.pop(index)
        raise IndexError(f'Индекс {index} вне диапазона (0-{len(self._items)-1})')
    
    def sort(self, key: Optional[Callable[[T], Any]] = None) -> None:
        """Сортирует коллекцию."""
        if key:
            self._items.sort(key=key)
        else:
            self._items.sort()
    
    #Магические методы
    
    def __len__(self) -> int:
        """Поддержка len()"""
        return self.size()
    
    def __str__(self) -> str:
        """Строковое представление коллекции"""
        return f"TypedCollection({self._items})"
    
    def __iter__(self) -> Iterator[T]:
        """Поддержка итерации"""
        return iter(self._items)
    
    def __getitem__(self, index: int) -> T:
        """Поддержка индексации"""
        return self._items[index]