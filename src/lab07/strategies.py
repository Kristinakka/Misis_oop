from base import Firearms, Edged


# --- Стратегии сортировки ---

def by_name(weapon):
    return weapon._imia

def by_damage(weapon):
    return weapon._damage

def by_rarity(weapon):
    rarity_order = {'Легендарное': 6, 'Мифическое': 5, 'Эпическое': 4,
                    'Сверхредкое': 3, 'Редкое': 2, 'Обычное': 1}
    return rarity_order.get(weapon._rare, 0)

def by_damage_then_name(weapon):
    return (weapon._damage, weapon._imia)

def by_price(weapon):
    return weapon.calculate_price()


# --- Функции-фильтры ---

def is_legendary(weapon):
    return weapon._rare == 'Легендарное'

def is_high_damage(weapon, min_damage=100):
    return weapon._damage >= min_damage

def is_repairable(weapon):
    return weapon._hardness < 100

def is_firearms(weapon):
    return isinstance(weapon, Firearms)

def is_edged(weapon):
    return isinstance(weapon, Edged)


# --- Фабрики фильтров ---

def make_damage_filter(min_damage, max_damage=None):
    def filter_fn(weapon):
        if max_damage is None:
            return weapon._damage >= min_damage
        return min_damage <= weapon._damage <= max_damage
    return filter_fn

def make_rarity_filter(rare_level):
    def filter_fn(weapon):
        return weapon._rare == rare_level
    return filter_fn

def make_price_multiplier(multiplier):
    def apply_multiplier(weapon):
        return weapon.calculate_price() * multiplier
    return apply_multiplier


# --- Функции для map ---

def to_string(weapon):
    return str(weapon)

def to_info_dict(weapon):
    return {
        'name': weapon._imia,
        'damage': weapon._damage,
        'rarity': weapon._rare,
        'price': weapon.calculate_price()
    }

def apply_discount(percent):
    def discount_fn(weapon):
        original_price = weapon.calculate_price()
        discounted_price = original_price * (1 - percent / 100)
        return (weapon._imia, original_price, discounted_price)
    return discount_fn


# --- Паттерн «Стратегия» через callable-объекты ---

class DamageUpgradeStrategy:
    def __init__(self, bonus_damage):
        self.bonus_damage = bonus_damage

    def __call__(self, weapon):
        old_damage = weapon._damage
        weapon._damage += self.bonus_damage
        return f"{weapon._imia}: урон повышен с {old_damage} до {weapon._damage}"


class RarityUpgradeStrategy:
    rarity_order = ['Обычное', 'Редкое', 'Сверхредкое', 'Эпическое', 'Мифическое', 'Легендарное']

    def __call__(self, weapon):
        old_rarity = weapon._rare
        if old_rarity in self.rarity_order:
            idx = self.rarity_order.index(old_rarity)
            if idx < len(self.rarity_order) - 1:
                weapon._rare = self.rarity_order[idx + 1]
                return f"{weapon._imia}: редкость повышена с {old_rarity} до {weapon._rare}"
        return f"{weapon._imia} уже имеет максимальную редкость!"


class RepairStrategy:
    def __call__(self, weapon):
        if weapon._hardness < 100:
            weapon._hardness = 100
            return f"{weapon._imia}: отремонтировано!"
        return f"{weapon._imia}: уже в идеальном состоянии"
