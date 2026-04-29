import sys
sys.path.append(r'C:\Users\Krist\OneDrive\Рабочий стол\Misis_oop\src\lab01')
from model import Weapon
from collection import Inventory 

def main():
    sword = Weapon(
        damage=20, 
        rare="Обычное", 
        hardness=50, 
        effects="кровотечение",  
        tip="Меч", 
        imia="Меч разбойника", 
        kolichestvo=1)
    bow = Weapon()
    dagger = Weapon("Кинжал", 8, 3)
    
   
    inventory = Inventory()
   
    inventory.add(sword)
    inventory.add(bow)
    inventory.add(dagger)
    
    print(" Все предметы в инвентаре")
    for item in inventory.get_all():
        print(f"{item._imia}: урон {item._damage}")
    

    print(" Использование for (__iter__)")
    for item in inventory:
        print(f"- {item._imia}")
    
    print(f"Количество предметов: {len(inventory)}  ")
    

    print(" Поиск по имени 'Лук'")
    found = inventory.find_by_name("Лук")
    if found:
        print(f"Найдено: {found._imia}, урон {found._damage}")
    else:
        print("Не найдено")
    
  
    print("\n=== Удаляем 'Кинжал' ===")
    inventory.remove(dagger)
    
    print("Инвентарь после удаления:")
    for item in inventory:
        print(f"- {item._imia}")
    
    print(f"Количество предметов после удаления: {len(inventory)}")
    
  
    print(" Пытаемся добавить дубликат 'Меч'")
    another_sword = Weapon("Меч", 20, 10)  
    try:
        inventory.add(another_sword)
        print("Дубликат добавился! (ОШИБКА - так не должно быть)")
    except ValueError as e:
        print(f"Ошибка (как и ожидалось): {e}")
    
    print("Пытаемся добавить не-Weapon объект")
    try:
        inventory.add("Это строка, не оружие")
        print("Неправильный тип добавился! (ОШИБКА)")
    except TypeError as e:
        print(f"Ошибка (как и ожидалось): {e}")

if __name__ == "__main__":
    main()