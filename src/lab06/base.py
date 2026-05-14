from model import Weapon

class Firearms(Weapon):
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

    def display_info(self):
        return f"{self._imia}, Калибр: {self._caliber}мм, {self._magazine_capacity} патронов, Урон: {self._damage}"
    

class Edged(Weapon):
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

    def display_info(self):
        return f"{self._imia}, {self._material}, {self._blade_length}см, Урон: {self._damage}"
    

    
    def display(self) -> str:       #Переопределяет метод родителя для огнестрельного оружия
        return f"{self._imia}, Калибр: {self._caliber}мм, Магазин: {self._magazine_capacity}, Урон: {self._damage}"

    def score(self) -> float:       #Переопределяет метод родителя с учетом специфики огнестрельного оружия
        base_score: float = super().score()
        caliber_bonus: float = (self._caliber / 20) * 10
        mag_bonus: float = (self._magazine_capacity / 100) * 10
        return min(base_score + caliber_bonus + mag_bonus, 100.0)