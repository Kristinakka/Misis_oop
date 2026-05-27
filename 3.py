def validate_name(name: str) -> str:
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("имя не может быть пустым")
    return cleaned


def validate_max_health(max_health: int) -> int:
    if not isinstance(max_health, int) or max_health <= 0:
        raise ValueError("max_health должно быть положительным целым числом")
    return max_health


def validate_level(level: int) -> int:
    if not isinstance(level, int) or not (1 <= level <= 100):
        raise ValueError("level должно быть целым числом от 1 до 100")
    return level


def validate_experience(experience: int) -> int:
    if not isinstance(experience, int) or experience < 0:
        raise ValueError("experience должно быть целым неотрицательным числом")
    return experience





class Character:
    def __init__(self, name: str, max_health: int, level: int = 1, experience: int = 0):
        
        self._name = validate_name(name)
        self._level = validate_level(level)
        self._experience = validate_experience(experience)
        self._max_health = validate_max_health(max_health)
        self._health = self._max_health
      

    @property
    def name(self) -> str: #Имя 
        return self._name

    @property
    def health(self) -> int: #Текущее здоровье
        return self._health

    @property
    def max_health(self) -> int: #Максимальное здоровье
        return self._max_health

    @property
    def level(self) -> int: #Уровень персонажа
        return self._level

    @property
    def experience(self) -> int: #Очки опыта
        return self._experience
    
    def take_damage(self, amount: int):
        if amount <= 0:
            raise ValueError("amount должен быть больше 0")
        self._health = max(0, self._max_health - amount)

    def heal(self, amount: int):
        if amount <= 0:
            raise ValueError("amount должен быть больше 0")
        self._health = min(self._max_health, self._health + amount)


    def gain_xp(self, amount: int):
        if amount < 0:
            raise ValueError("amount должен быть >= 0")

        self._experience += amount

        #Повышение уровня, пока опыта хватает
        while self._experience >= self._level * 100:
            self._experience -= self._level * 100  # вычитаем порог
            if self._level < 100:
                self._level += 1
            else: #На максимальном уровне опыт больше не повышает уровень
                break


    def is_alive(self) -> bool:
        return self._health > 0
    

    
    #Магические методы
    def __str__(self) -> str:
        return f"Воин (уровень {self._level}): {self._health}{self._max_health} HP, XP {self._experience}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Character):
            return False
        return self._name == other._name
    


hero = Character('Воин', 100, 1, 0)
hero.take_damage(30)
print(hero.health)       # 70
hero.heal(20)
print(hero.health)       # 90
hero.gain_xp(150)
print(hero.level)        # 2  (преодолел 100)
print(hero.experience)   # 50

Character('', 100)            # ValueError: имя пустое
Character('Воин', 0)          # ValueError: max_health > 0
hero.take_damage(-5)          # ValueError: amount > 0
