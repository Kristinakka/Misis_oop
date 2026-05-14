import sys
sys.path.append(r'C:\Users\Krist\OneDrive\Рабочий стол\Misis_oop\src\lab04')

from models import Firearms, Edged, Inventory
from interfaces import Printable, Repairable, Comparable

print("ЛАБОРАТОРНАЯ РАБОТА №4 - ИНТЕРФЕЙСЫ")

# Создаем инвентарь
inventory = Inventory()

# Создаем оружие
cheremsha = Firearms(
    damage=75, rare="Редкое", hardness=100, effects="кровотечение",
    tip="Пушка", imia="Черемша", kolichestvo=100,
    caliber=7.62, magazine_capacity=30
)

anastasia = Edged(
    damage=150, rare="Легендарное", hardness=100, effects="свет, огонь",
    tip="Меч", imia="Анастасия", kolichestvo=1,
    blade_length=120, material="хз"
)

hamam = Edged(
    damage=90, rare="Редкое", hardness=100, effects="острота",
    tip="Топор", imia="Хамам", kolichestvo=1,
    blade_length=75, material="давлат"
)

# Добавляем в инвентарь
inventory.add(cheremsha)
inventory.add(anastasia)
inventory.add(hamam)


print("\n СЦЕНАРИЙ 1: Интерфейс Printable")

print("Вывод информации через get_info() (разная реализация):")
inventory.print_all_info()


print("\nСЦЕНАРИЙ 2: Интерфейс Repairable")
print("Ломаем Черемшу...")
for _ in range(101):
    cheremsha.attack()
print(cheremsha.status)
print(f"Ремонт: {cheremsha.repair_weapon()}")
print(cheremsha.status)


print("\n СЦЕНАРИЙ 3: Интерфейс Comparable")
print("Сортировка по урону через compare_to():")
print("До сортировки:")
for item in inventory.items:
    print(f"  {item._imia}: урон {item._damage}")

inventory.sort_by_damage()
print("\nПосле сортировки:")
for item in inventory.items:
    print(f"  {item._imia}: урон {item._damage}")


print("\n СЦЕНАРИЙ 4: Фильтрация через isinstance")

print(f"Черемша реализует Printable? {isinstance(cheremsha, Printable)}")
print(f"Черемша реализует Repairable? {isinstance(cheremsha, Repairable)}")
print(f"Черемша реализует Comparable? {isinstance(cheremsha, Comparable)}")
print(f"\nАнастасия реализует Printable? {isinstance(anastasia, Printable)}")
print(f"Анастасия реализует Repairable? {isinstance(anastasia, Repairable)}")
print(f"Анастасия реализует Comparable? {isinstance(anastasia, Comparable)}")
print(f"\nХамам реализует Printable? {isinstance(hamam, Printable)}")
print(f"Хамам реализует Repairable? {isinstance(hamam, Repairable)}")
print(f"Хамам реализует Comparable? {isinstance(hamam, Comparable)}")

print("\n Только Printable объекты:")
printable_items = inventory.get_printable_items()
for item in printable_items.items:
    print(f"  {item.get_info()}")

print("\nСЦЕНАРИЙ 5: Универсальная функция через интерфейс")

def print_all_weapons(weapon_list):
    """Функция работает с любыми объектами, реализующими Printable"""
    for item in weapon_list:
        if isinstance(item, Printable):
            print(f" {item.get_info()}")

print("Вызов универсальной функции:")
print_all_weapons(inventory.items)


print("\n СЦЕНАРИЙ 6: Множественная реализация интерфейсов")
print("Оба класса реализуют ВСЕ три интерфейса:")
print(f"Firearms: Printable | Repairable | Comparable ")
print(f"Edged: Printable | Repairable | Comparable ")
print("\nРазная реализация get_info():")
print(f"Firearms (Черемша): {cheremsha.get_info()}")
print(f"Edged (Анастасия): {anastasia.get_info()}")
print(f"Edged (Хамам): {hamam.get_info()}")
print("\nРазная реализация repair_weapon():")
print(f"Firearms (Черемша): {cheremsha.repair_weapon()}")
print(f"Edged (Анастасия): {anastasia.repair_weapon()}")
print(f"Edged (Хамам): {hamam.repair_weapon()}")


print("ВСЕ!")
