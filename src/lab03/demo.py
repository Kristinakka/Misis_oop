from models import Weapon
from base import Firearms
from base import Edged
from collections import Inventory

def main():

    print("\n1. СОЗДАНИЕ ОБЪЕКТОВ РАЗНЫХ ТИПОВ")

    basic_sword = Weapon(15, "обычное", 100, "нет", "меч", "Простой меч", 1)
    print(f"Базовый: {basic_sword}")

    ak47 = Firearms(45, "редкое", 85, "отдача", "автомат", "АК-47", 100,
                    caliber=7.62, magazine_capacity=30)
    print(f"Огнестрельное: {ak47}")
    
    excalibur = Edged(60, "легендарное", 100, "светится", "меч", "Экскалибур", 1,
                      blade_length=90, material="дамасская сталь")
    print(f"Холодное: {excalibur}")

    #СЦЕНАРИЙ 2: НОВЫЕ МЕТОДЫ ДОЧЕРНИХ КЛАССОВ
    print("\n2. НОВЫЕ МЕТОДЫ ДОЧЕРНИХ КЛАССОВ")
    print("-" * 40)
    print(f"Firearms.reload(): {ak47.reload()}")
    print(f"Edged.sharpen(): {excalibur.sharpen()}")

    #СЦЕНАРИЙ 3: МЕТОДЫ БАЗОВОГО КЛАССА 
    print("\n3. МЕТОДЫ БАЗОВОГО КЛАССА")
    print(f"attack(): {ak47.attack()}")
    print(f"attack(): {ak47.attack()}")  
    print(f"repair(): {ak47.repair()}")
    print(f"status: {ak47.status}")

    # СЦЕНАРИЙ 4: ПОЛИМОРФИЗМ calculate_price()
    print("\n4. ПОЛИМОРФИЗМ - calculate_price()")
  
    
    # Создаем список объектов разных типов
    weapons_list = [basic_sword, ak47, excalibur]
    
    for w in weapons_list:
        if hasattr(w, 'calculate_price'):
            print(f"{w.imia}: {w.calculate_price()} монет")
        else:
            price = w._damage * 10
            if w._rare == 'легендарное':
                price *= 3
            elif w._rare == 'редкое':
                price *= 2
            print(f"{w.imia}: {price} монет (базовый расчет)")

    #СЦЕНАРИЙ 5: РАБОТА С КОЛЛЕКЦИЕЙ 
    print("\n5. КОЛЛЕКЦИЯ ОРУЖИЯ (смешанные типы)")

    collection = WeaponCollection()
    collection.add(basic_sword)
    collection.add(ak47)
    collection.add(excalibur)

    glock = Firearms(30, "обычное", 95, "нет", "пистолет", "Glock-17", 50,
                     caliber=9, magazine_capacity=17)
    katana = Edged(50, "редкое", 100, "острое", "катана", "Мурамаса", 1,
                   blade_length=75, material="булат")

    collection.add(glock)
    collection.add(katana)

    print(f"Всего в коллекции: {len(collection)} предметов")
    collection.display_all()

    #СЦЕНАРИЙ 6: ФИЛЬТРАЦИЯ ПО ТИПУ (isinstance)
    print("\n6. ФИЛЬТРАЦИЯ С ПОМОЩЬЮ isinstance()")

    firearms_only = collection.get_firearms()
    print(f"Огнестрельное оружие ({len(firearms_only)} шт.):")
    for f in firearms_only:
        print(f"  - {f.imia}")

    edged_only = collection.get_edged()
    print(f"\nХолодное оружие ({len(edged_only)} шт.):")
    for e in edged_only:
        print(f"  - {e.imia}")

    #СЦЕНАРИЙ 7: ПОЛИМОРФИЗМ БЕЗ УСЛОВИЙ (display_info)
    print("\n7. ПОЛИМОРФИЗМ БЕЗ УСЛОВИЙ")
    print("Вызов display_info() для всех объектов в коллекции:")
    for weapon in collection.get_all():
        if hasattr(weapon, 'display_info'):
            print(f"  {weapon.display_info()}")
        else:
            print(f"  {weapon}")

    #СЦЕНАРИЙ 8: СУММАРНАЯ СТОИМОСТЬ КОЛЛЕКЦИИ
    print("\n8. СУММАРНАЯ СТОИМОСТЬ КОЛЛЕКЦИИ")
    total = collection.calculate_total_price()
    print(f"Общая стоимость всей коллекции: {total} монет")

    for weapon in collection.get_all():
        if hasattr(weapon, 'calculate_price'):
            print(f"  {weapon.imia}: {weapon.calculate_price()} монет")
        else:
            price = weapon._damage * 10
            if weapon._rare == 'легендарное':
                price *= 3
            elif weapon._rare == 'редкое':
                price *= 2
            print(f"  {weapon.imia}: {price} монет")

    #ПРОВЕРКА ТИПОВ
    print("\n9. ПРОВЕРКА ТИПОВ С ПОМОЩЬЮ isinstance()")
    print(f"ak47 является Firearms? {isinstance(ak47, Firearms)}")
    print(f"ak47 является Weapon? {isinstance(ak47, Weapon)}")
    print(f"excalibur является Edged? {isinstance(excalibur, Edged)}")
    print(f"basic_sword является Firearms? {isinstance(basic_sword, Firearms)}")
    print(f"basic_sword является Weapon? {isinstance(basic_sword, Weapon)}")

    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")



if __name__ == "__main__":
    main()