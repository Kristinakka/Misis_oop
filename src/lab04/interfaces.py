from abc import ABC, abstractmethod

class Printable(ABC):
    """Интерфейс для вывода информации об оружии"""
    @abstractmethod
    def get_info(self) -> str:
        pass

class Repairable(ABC):
    """Интерфейс для ремонта оружия"""
    @abstractmethod
    def repair_weapon(self) -> str:
        pass

class Comparable(ABC):
    """Интерфейс для сравнения оружия по урону"""
    @abstractmethod
    def compare_to(self, other) -> int:
        pass