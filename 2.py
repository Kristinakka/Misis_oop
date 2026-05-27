import random
from abc import ABC, abstractmethod
from typing import List

#Собственное исключение
class InsufficientManaError(Exception):
    pass


# Шаг 1: Интерфейс стратегии атаки
class AttackStrategy(ABC):
    @abstractmethod
    def attack(self, attacker, target):
        pass

# Шаг 2: Конкретные стратегии
class SwordAttack(AttackStrategy):
    def __init__(self, damage):
        self.damage = damage
    
    def attack(self, attacker, target):
        target.take_damage(self.damage)


class BowAttack(AttackStrategy):
    def __init__(self, damage, accuracy):
        self.damage = damage
        self.accuracy = accuracy
        def attack(self, attacker, target):
            if random.random() < self.accuracy:
                target.take_damage(self.damage)


class MagicAttack(AttackStrategy):
    def __init__(self, damage, mana_cost):
        self.damage = damage
        self.mana_cost = mana_cost
    
    def attack(self, attacker, target):
        if attacker.experience < self.mana_cost:
            raise InsufficientManaError(f"Недостаточно опыта! Нужно {self.mana_cost}, есть {attacker.experience}")
        attacker._experience -= self.mana_cost
        target.take_damage(self.damage)


class CriticalAttack(AttackStrategy):
    def __init__(self, base_damage, crit_multiplier):
        self.base_damage = base_damage
        self.crit_multiplier = crit_multiplier
    
    def attack(self, attacker, target):
        if attacker.level % 2 == 0:  # чётный уровень
            damage = self.base_damage * self.crit_multiplier
        else:  # нечётный уровень
            damage = self.base_damage
        target.take_damage(damage)




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
        self._max_health = validate_max_health(max_health)
        self.level = validate_level(level)
        self._experience = validate_experience(experience)
        self._max_health = validate_max_health(max_health)
        self._attack_strategy = None

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
        self._health = max(0, self._health - amount)

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
    

    def set_attack_strategy(self, strategy: AttackStrategy): #Устанавливает стратегию атаки
        self._attack_strategy = strategy

    def attack(self, target): #Атакует цель, используя текущую стратегию
        if self._attack_strategy is None:
            raise ValueError("Стратегия атаки не установлена")
        self._attack_strategy.attack(self, target)


    #Магические методы
    def __str__(self) -> str:
        return f"Воин (уровень {self._level}): {self._health}{self._max_health} HP, XP {self._experience}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Character):
            return False
        return self._name == other._name
    

#Шаг 4: Команда персонажей 
class Party:
    def __init__(self, characters: List[Character] = None):
        self._members = characters if characters else []

    def add(self, character: Character): #добавление персонажа
        self._members.append(character)

    def alive_members(self) -> List[Character]: #возврат списка живых персонажей
        return [member for member in self._members if member.is_alive()]

    def battle(self, other_party): #битва между командами
        team1 = self.alive_members()
        team2 = other_party.alive_members()
    
        while team1 and team2: #каждый живой из первой команды атакует случайного живого из второй
            for attacker in team1[:]:  #копия списка
                if not team2:  #если вторая команда уже мертва
                    break
                target = random.choice(team2)
                attacker.attack(target) #Обновляем списки живых
                team2 = other_party.alive_members()
                if not team2:
                    break
            
            #Обновляем списки живых после атаки первой команды
            team1 = self.alive_members()
            team2 = other_party.alive_members()
            
            if not team2:
                break 
            # Каждый живой из второй команды атакует случайного живого из первой
            for attacker in team2[:]:
                if not team1:
                    break
                target = random.choice(team1)
                attacker.attack(target)
                team1 = self.alive_members()
                if not team1:
                    break
            
            # Обновляем списки живых
            team1 = self.alive_members()
            team2 = other_party.alive_members()


