import sys
sys.path.append(r'C:\Users\Krist\OneDrive\Рабочий стол\Misis_oop\src\lab05')

from models import Firearms, Edged
from collection import Inventory
from strategies import *



inventory = Inventory()


weapons = [
    Firearms(damage=75, rare="редкое", hardness=100, effects="кровотечение",
             tip="автомат", imia="Черемша", kolichestvo=100,
             caliber=7.62, magazine_capacity=30),
    
    Edged(damage=150, rare="легендарное", hardness=100, effects="свет, огонь",
          tip="меч", imia="Анастасия", kolichestvo=1,
          blade_length=120, material="кдчд"),
    
    Edged(damage=90, rare="редкое", hardness=100, effects="острота",
          tip="катана", imia="Хамам", kolichestvo=1,
          blade_length=75, material="хз"),
    
    Firearms(damage=45, rare="обычное", hardness=80, effects="нет",
             tip="пистолет", imia="Глок-17", kolichestvo=50,
             caliber=9.0, magazine_capacity=17),
    
    Edged(damage=60, rare="обычное", hardness=90, effects="кровотечение",
          tip="кинжал", imia="Тень", kolichestvo=3,
          blade_length=30, material="титан"),
    
    Firearms(damage=120, rare="легендарное", hardness=100, effects="взрыв",
             tip="дробовик", imia="Разрушитель", kolichestvo=1,
             caliber=12.0, magazine_capacity=8)
]

for w in weapons:
    inventory.add(w)

print(f"\nСоздана коллекция из {len(inventory)} предметов:")
for item in inventory.items:
    print(f"   - {item._imia} (урон: {item._damage}, редкость: {item._rare})")


print("СЦЕНАРИЙ 1: ТРИ СТРАТЕГИИ СОРТИРОВКИ")

print("\n1️Сортировка по имени (by_name):")
inventory.sort_by(by_name)
for item in inventory.items:
    print(f"   - {item._imia}")

print("\n2️Сортировка по урону (by_damage):")
inventory.sort_by(by_damage)
for item in inventory.items:
    print(f"   - {item._imia}: урон {item._damage}")

print("\n3️Сортировка по редкости (by_rarity):")
inventory.sort_by(by_rarity, reverse=True)  # reverse=True для Legendary сначала
for item in inventory.items:
    print(f"   - {item._imia}: {item._rare}")


print("СЦЕНАРИЙ 2: ФИЛЬТРАЦИЯ КОЛЛЕКЦИИ")

print("\nФильтр 1: Только легендарное оружие (is_legendary):")
legendary_items = inventory.filter_by(is_legendary)
for item in legendary_items.items:
    print(f"   - {item._imia}: {item._rare}")

print("\nФильтр 2: Оружие с уроном >= 100 (is_high_damage):")
high_damage_items = inventory.filter_by(lambda x: is_high_damage(x, min_damage=100))
for item in high_damage_items.items:
    print(f"   - {item._imia}: урон {item._damage}")


print("СЦЕНАРИЙ 3: ПРЕОБРАЗОВАНИЕ КОЛЛЕКЦИИ ЧЕРЕЗ map()")

print("\nПреобразование в список названий (lambda):")
names = inventory.map_to(lambda x: x._imia)
print(f"   Названия: {names}")

print("\nПрименение скидки 20% ко всем товарам:")
discount_20 = apply_discount(20)
discounted_prices = inventory.map_to(discount_20)
for name, original, discounted in discounted_prices:
    print(f"   - {name}: {original} → {discounted} (скидка 20%)")

print("\nПреобразование в словари (to_info_dict):")
info_dicts = inventory.map_to(to_info_dict)
for d in info_dicts:
    print(f"   - {d['name']}: урон {d['damage']}, цена {d['price']}")


print("СЦЕНАРИЙ 4: ФАБРИКА ФУНКЦИЙ")

print("\nСоздаём фильтр через фабрику make_damage_filter(80, 120):")
damage_filter = make_damage_filter(80, 120)
filtered_inventory = inventory.filter_by(damage_filter)
print(f"   Оружие с уроном от 80 до 120:")
for item in filtered_inventory.items:
    print(f"   - {item._imia}: урон {item._damage}")

print("\nСоздаём фильтр для легендарного оружия через фабрику:")
legendary_filter = make_rarity_filter('легендарное')
legendary_items = inventory.filter_by(legendary_filter)
for item in legendary_items.items:
    print(f"   - {item._imia}: {item._rare}")



print("СЦЕНАРИЙ 5: ПАТТЕРН 'СТРАТЕГИЯ' ЧЕРЕЗ CALLABLE-ОБЪЕКТЫ")
# Создаем копию коллекции для демонстрации
test_inventory = Inventory()
for w in weapons[:3]:  # берем первые 3 оружия
    test_inventory.add(w)

print("\nИсходная коллекция:")
for item in test_inventory.items:
    print(f"   - {item._imia}: урон {item._damage}, редкость {item._rare}")

print("\nПрименяем стратегию DamageUpgradeStrategy (+20 к урону):")
upgrade_strategy = DamageUpgradeStrategy(20)
results = test_inventory.apply(upgrade_strategy)
for result in results:
    print(f"   {result}")

print("\nПрименяем стратегию RarityUpgradeStrategy:")
rarity_strategy = RarityUpgradeStrategy()
results = test_inventory.apply(rarity_strategy)
for result in results:
    print(f"   {result}")

print("\nПрименяем стратегию RepairStrategy:")
repair_strategy = RepairStrategy()
test_inventory.apply(repair_strategy)


print("СЦЕНАРИЙ 6: ЦЕПОЧКА ОПЕРАЦИЙ filter → sort → apply")

print("\nЦепочка: filter_by(legendary) → sort_by(damage) → apply(upgrade)")
result = (inventory.chain()
          .filter_by(is_legendary)
          .sort_by(by_damage, reverse=True)
          .apply(DamageUpgradeStrategy(50)))

print("\nРезультаты применения цепочки:")
for r in result:
    print(f"   {r}")

print("\nДругая цепочка: filter_by(high_damage) → sort_by(name) → map_to(name)")
chain_result = (inventory.chain()
                .filter_by(lambda x: is_high_damage(x, min_damage=80))
                .sort_by(by_name)
                .map_to(lambda x: x._imia))

print(f"\n   Отфильтрованные и отсортированные названия: {chain_result}")


print("СЦЕНАРИЙ 7: LAMBDA vs ИМЕНОВАННАЯ ФУНКЦИЯ")

print("\nСортировка через lambda (анонимная функция):")
inventory.sort_by(lambda x: x._damage, reverse=True)
for item in inventory.items[:3]:
    print(f"   - {item._imia}: урон {item._damage}")

print("\nСортировка через именованную функцию (by_damage):")
inventory.sort_by(by_damage, reverse=True)
for item in inventory.items[:3]:
    print(f"   - {item._imia}: урон {item._damage}")

print("\nФильтрация через lambda:")
cheap_filter = inventory.filter_by(lambda x: x.calculate_price() < 500)
print(f"   Оружие дешевле 500: {len(cheap_filter.items)} шт.")

print("\nФильтрация через именованную функцию (is_legendary):")
legendary_only = inventory.filter_by(is_legendary)
print(f"Легендарное оружие: {len(legendary_only.items)} шт.")


# итог
print("ВСЕ ТРЕБОВАНИЯ ВЫПОЛНЕНЫ!")
print("\nВыполненные пункты:")
print("3+ стратегии сортировки (by_name, by_damage, by_rarity, by_price)")
print("2+ функции-фильтра (is_legendary, is_high_damage)")
print("Использование map(), filter(), sorted()")
print("Фабрика функций (make_damage_filter, make_rarity_filter)")
print("Методы sort_by() и filter_by() в коллекции")
print("Lambda-выражения")
print("Паттерн 'Стратегия' через callable-объекты")
print("Метод apply() в коллекции")
print("Цепочка операций (chain)")
print("Все стратегии в отдельном файле strategies.py")