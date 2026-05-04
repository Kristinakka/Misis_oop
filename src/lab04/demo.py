import sys
sys.path.append(r'C:\Users\Krist\OneDrive\Рабочий стол\Misis_oop\src\lab04')

from models import Firearms, Edged, Inventory
from interfaces import Printable, Repairable, Comparable

print("ЛАБОРАТОРНАЯ РАБОТА №4 - ИНТЕРФЕЙСЫ")

# Создаем инвентарь
inventory = Inventory()

# Создаем оружие
ak47 = Firearms(
    damage=75, rare="редкое", hardness=100, effects="кровотечение",
    tip="автомат", imia="АК-47", kolichestvo=100,
    caliber=7.62, magazine_capacity=30
)

excalibur = Edged(
    damage=150, rare="легендарное", hardness=100, effects="свет, огонь",
    tip="меч", imia="Экскалибур", kolichestvo=1,
    blade_length=120, material="хз"
)

katana = Edged(
    damage=90, rare="редкое", hardness=100, effects="острота",
    tip="катана", imia="Черемша", kolichestvo=1,
    blade_length=75, material="кдчд"
)

# Добавляем в инвентарь
inventory.add(ak47)
inventory.add(excalibur)
inventory.add(katana)

# ========== СЦЕНАРИЙ 1: интерфейс Printable ==========
print("\nСЦЕНАРИЙ 1: Интерфейс Printable")
print("Вывод информации через get_info() (разная реализация):")
inventory.print_all_info()

# ========== СЦЕНАРИЙ 2: интерфейс Repairable ==========
print("\n2️СЦЕНАРИЙ 2: Интерфейс Repairable")
print("Ломаем АК-47")
for _ in range(101):
    ak47.attack()
print(ak47.status)
print(f"Ремонт: {ak47.repair_weapon()}")
print(ak47.status)

# ========== СЦЕНАРИЙ 3: интерфейс Comparable ==========
print("\nСЦЕНАРИЙ 3: Интерфейс Comparable")
print("Сортировка по урону через compare_to():")
print("До сортировки:")
for item in inventory.items:
    print(f"  {item._imia}: урон {item._damage}")

inventory.sort_by_damage()
print("\nПосле сортировки:")
for item in inventory.items:
    print(f"  {item._imia}: урон {item._damage}")

# ========== СЦЕНАРИЙ 4: isinstance и фильтрация ==========
print("\nСЦЕНАРИЙ 4: Фильтрация через isinstance)
print(f"АК-47 реализует Printable? {isinstance(ak47, Printable)}")
print(f"АК-47 реализует Repairable? {isinstance(ak47, Repairable)}")
print(f"АК-47 реализует Comparable? {isinstance(ak47, Comparable)}")
print(f"\nЭкскалибур реализует Printable? {isinstance(excalibur, Printable)}")
print(f"Экскалибур реализует Repairable? {isinstance(excalibur, Repairable)}")
print(f"Экскалибур реализует Comparable? {isinstance(excalibur, Comparable)}")

print("\n📦 Только Printable объекты:")
printable_items = inventory.get_printable_items()
for item in printable_items.items:
    print(f"  {item.get_info()}")

# ========== СЦЕНАРИЙ 5: универсальная функция ==========
print("\n5️⃣ СЦЕНАРИЙ 5: Универсальная функция через интерфейс")

def print_all_weapons(weapon_list):
    """Функция работает с любыми объектами, реализующими Printable"""
    for item in weapon_list:
        if isinstance(item, Printable):
            print(f"  📄 {item.get_info()}")

print("Вызов универсальной функции:")
print_all_weapons(inventory.items)

# ========== СЦЕНАРИЙ 6: множественная реализация ==========
print("\n6️⃣ СЦЕНАРИЙ 6: Множественная реализация интерфейсов")
print("Оба класса реализуют ВСЕ три интерфейса:")
print(f"  Firearms: Printable ✅ | Repairable ✅ | Comparable ✅")
print(f"  Edged:    Printable ✅ | Repairable ✅ | Comparable ✅")
print("\nРазная реализация get_info():")
print(f"  Firearms: {ak47.get_info()}")
print(f"  Edged:    {excalibur.get_info()}")
print("\nРазная реализация repair_weapon():")
print(f"  Firearms: {ak47.repair_weapon()}")
print(f"  Edged:    {excalibur.repair_weapon()}")