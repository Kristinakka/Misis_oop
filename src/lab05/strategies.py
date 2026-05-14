from .base import Firearms, Edged
# стратегии сортировки

def by_name(weapon): # стратегия соортировки по имени 
    return weapon._imia

def by_damage(weapon): #стратегия сортировки по урону
    return weapon._damage

def by_rarity(weapon): # cтратегия сортировки по редкости (легендарное > редкое > обычное)
    rarity_order = {'легендарное': 3, 'редкое': 2, 'обычное': 1}
    return rarity_order.get(weapon._rare, 0)

def by_damage_then_name(weapon): # cтратегия сортировки сначала по урону, затем по имени
    return (weapon._damage, weapon._imia)

def by_price(weapon): # cтратегия сортировки по цене
    return weapon.calculate_price()


# функции-фильтры

def is_legendary(weapon): # только легенда
    return weapon._rare == 'легендарное'

def is_high_damage(weapon, min_damage=100): # оружие только с уроном выше порога
    return weapon._damage >= min_damage

def is_repairable(weapon): # оружие, которое надо починить 
    return weapon._hardness < 100

def is_firearms(weapon): # только огнестрельное
    return isinstance(weapon, Firearms)  

def is_edged(weapon): # только холодное оружие
    return isinstance(weapon, Edged)


# смотря какой fabric функции

def make_damage_filter(min_damage, max_damage=None):
    """
    Фабрика функций: создаёт фильтр по диапазону урона
    
    Параметры:
        min_damage: минимальный урон
        max_damage: максимальный урон (опционально)
    
    Возвращает функцию-фильтр
    """
    def filter_fn(weapon):
        if max_damage is None:
            return weapon._damage >= min_damage
        return min_damage <= weapon._damage <= max_damage
    return filter_fn

def make_rarity_filter(rare_level):
    """
    Фабрика функций: создаёт фильтр по редкости
    
    Параметры:
        rare_level: строка с редкостью ('легендарное', 'редкое', 'обычное')
    
    Возвращает функцию-фильтр
    """
    def filter_fn(weapon):
        return weapon._rare == rare_level
    return filter_fn

def make_price_multiplier(multiplier):
    """
    Фабрика функций: создаёт функцию для изменения цены
    
    Параметры:
        multiplier: множитель цены
    
    Возвращает функцию преобразования
    """
    def apply_multiplier(weapon):
        original_price = weapon.calculate_price()
        return original_price * multiplier
    return apply_multiplier


# функции для Map

def to_string(weapon): # оружие в строку делат
    return str(weapon)

def to_info_dict(weapon): # оружие в словар делат
    return {
        'name': weapon._imia,
        'damage': weapon._damage,
        'rarity': weapon._rare,
        'price': weapon.calculate_price()
    }

def apply_discount(percent):
    """
    Фабрика функций: создаёт функцию для применения скидки
    
    Параметры:
        percent: процент скидки (0-100)
    
    Возвращает функцию, которая изменяет цену оружия
    """
    def discount_fn(weapon):
        original_price = weapon.calculate_price()
        discounted_price = original_price * (1 - percent / 100)
        return (weapon._imia, original_price, discounted_price)
    return discount_fn


# паттерн «Стратегия» через callable-объекты

class DamageUpgradeStrategy: # стратегия улучшения урона оружия
    def __init__(self, bonus_damage):
        self.bonus_damage = bonus_damage
    
    def __call__(self, weapon): # применяем стратегия к улучшению оружия  
        old_damage = weapon._damage
        weapon._damage += self.bonus_damage
        return f" {weapon._imia}: урон повышен с {old_damage} до матадора {weapon._damage}"


class RarityUpgradeStrategy: # улучшение редкости оружия 
    rarity_order = ['обычное', 'редкое', 'легендарное']
    
    def __call__(self, weapon):
        old_rarity = weapon._rare
        if old_rarity == 'обычное':
            weapon._rare = 'редкое'
        elif old_rarity == 'редкое':
            weapon._rare = 'легендарное'
        else:
            return f"{weapon._imia} уже имеет максимальную редкость!"
        
        return f"{weapon._imia}: редкость повышена с {old_rarity} до {weapon._rare}"


class RepairStrategy: # ремонт оружия
    def __call__(self, weapon):
        if weapon._hardness < 100:
            weapon._hardness = 100
            return f"{weapon._imia}: отремонтировано!"
        return f"{weapon._imia}: уже в идеальном состоянии"