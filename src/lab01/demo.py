from validate import *
from model import *
print("ТЕСТИРОВАНИЕ КЛАССА WEAPON")

# 1.СОЗДАНИЯ ОБЪЕКТОВ
print("ТЕСТ 1: Создание объектов")
# Сценарий 1
try:
    weapon1 = Weapon(
        damage=50, 
        rare="Легендарное",  
        hardness=100, 
        effects="огонь, лед", 
        tip="Меч",  
        imia="Экскалибур", 
        kolichestvo=1
    )
    print("Успешно создан объект weapon1:")
    print(f"{weapon1}")
except Exception as e:
    print(f"Ошибка при создании weapon1: {type(e).__name__}: {e}")

# Сценарий 2
try:
    weapon_invalid_name = Weapon(
        damage=30, 
        rare="Обычное", 
        hardness=80, 
        effects="", 
        tip="Лук", 
        imia="",  
        kolichestvo=2
    )
    print(f"Ошибка: Объект с пустым именем создан: {weapon_invalid_name}")
except Exception as e:
    print(f"Перехвачена ошибка при пустом имени: {type(e).__name__}: {e}")


try:
    weapon_invalid_damage = Weapon(
        damage=-10,  
        rare="Редкое", 
        hardness=90, 
        effects="яд", 
        tip="Топор", 
        imia="Секира", 
        kolichestvo=1
    )
    print(f"Ошибка: Объект с отрицательным уроном создан")
except Exception as e:
    print(f"Перехвачена ошибка при отрицательном уроне: {type(e).__name__}: {e}")

try:
    weapon_invalid_tip = Weapon(
        damage=40, 
        rare="Эпическое", 
        hardness=70, 
        effects="свет", 
        tip="Пистолет",  
        imia="Посох света", 
        kolichestvo=1
    )
    print(f"Ошибка: Объект с невалидным типом создан")
except Exception as e:
    print(f"Перехвачена ошибка при невалидном типе: {type(e).__name__}: {e}")


try:
    weapon_invalid_hardness = Weapon(
        damage=60, 
        rare="Легендарное", 
        hardness=150,  
        effects="взрыв", 
        tip="Копье", 
        imia="Громовержец", 
        kolichestvo=1
    )
    print(f"Ошибка: Объект с твердостью >100 создан")
except Exception as e:
    print(f"Перехвачена ошибка при твердости >100: {type(e).__name__}: {e}")


try:
    weapon_invalid_rare = Weapon(
        damage=20, 
        rare="Божественное",  
        hardness=50, 
        effects="кровотечение", 
        tip="Посох", 
        imia="Посох мага", 
        kolichestvo=1
    )
    print(f"Ошибка: Объект с невалидной редкостью создан")
except Exception as e:
    print(f"Перехвачена ошибка при невалидной редкости: {type(e).__name__}: {e}")


try:
    weapon_invalid_effects = Weapon(
        damage=20, 
        rare="Обычное", 
        hardness=50, 
        effects=["кровотечение"],  
        tip="Нож", 
        imia="Нож разбойника", 
        kolichestvo=1
    )
    print(f"Ошибка: Объект с effects-списком создан")
except Exception as e:
    print(f"Перехвачена ошибка при effects-списке: {type(e).__name__}: {e}")

# Если weapon1 создан, продолжаем тесты
if 'weapon1' in locals():
    print("ТЕСТ 2: Тестирование свойств (property)")
    
# Сценарий 3
    try:
        print(f"rename (геттер): {weapon1.rename}")
        print(f"status (геттер - только чтение): {weapon1.status}")
        print("Все геттеры работают корректно")
    except Exception as e:
        print(f"Ошибка при получении свойств: {type(e).__name__}: {e}")
    

    print("ТЕСТ 3: Сеттеры с корректными значениями")
    
    try:
        weapon1.rename = "Новый Экскалибур"
        print(f"rename изменено на: {weapon1.rename}")
    except Exception as e:
        print(f"Ошибка при изменении rename: {type(e).__name__}: {e}")
       
    
    print("ТЕСТ 4: Попытка изменить status (только для чтения)")
    try:
        weapon1.status = "Новый статус"  
        print("Ошибка: status удалось изменить!")
    except AttributeError:
        print("Правильно: status нельзя изменить (AttributeError)")
    except Exception as e:
        print(f"Неожиданная ошибка: {type(e).__name__}: {e}")
    
    
    print("ТЕСТ 5: Сеттеры с некорректными значениями")
    
    try:
        weapon1.rename = ""  # Пустое имя
        print("Ошибка: rename с пустой строкой принято")
    except Exception as e:
        print(f"rename: перехвачена ошибка - {type(e).__name__}: {e}")
        
    # ТЕСТИРОВАНИЕ МЕТОДОВ
    print("ТЕСТ 6: Тестирование методов класса")
    

    print("Тест attack():")
    for i in range(3):
        try:
            result = weapon1.attack()
            print(f"Атака {i+1}: {result}")
            print(f"Текущая твердость: {weapon1.hardness}")
        except Exception as e:
            print(f"Ошибка при атаке: {type(e).__name__}: {e}")       
    
    print("Тест repair():")
    try:
        weapon1.hardness = 0
        print(f"Твердость перед ремонтом: {weapon1.hardness}")
        print(f"Статус: {weapon1.status}")
        
        result = weapon1.repair()
        print(f"{result}")
        print(f"Твердость после ремонта: {weapon1.hardness}")
        print(f"Статус после ремонта: {weapon1.status}")
    except Exception as e:
        print(f"Ошибка при ремонте: {type(e).__name__}: {e}")
    
    
    print("Тест repair() при макс. прочности:")
    try:
        weapon1.hardness = 100
        result = weapon1.repair()
        print(f"{result}")
        print(f"Твердость: {weapon1.hardness}")
    except Exception as e:
        print(f"Ошибка: {type(e).__name__}: {e}")
    
    print("Тест __str__():")
    try:
        weapon1.hardness = 50
        print(f"{weapon1}")
        
        weapon1.hardness = 0
        print(f"{weapon1}")
    except Exception as e:
        print(f"Ошибка в __str__: {type(e).__name__}: {e}")
    

    print("Тест __repr__():")
    try:
        print(f"{repr(weapon1)}")
    except Exception as e:
        print(f"Ошибка в __repr__: {type(e).__name__}: {e}")
    

    print("Тест __eq__():")
    try:
        weapon2 = Weapon(
            damage=30, 
            rare="Обычное", 
            hardness=100, 
            effects="огонь", 
            tip="Топор",  
            imia="Простой топор", 
            kolichestvo=2
        )
        weapon3 = Weapon(
            damage=40, 
            rare="Редкое", 
            hardness=90, 
            effects="лед", 
            tip="Лук",  
            imia="Лук охотника", 
            kolichestvo=1
        )
        
        print(f"weapon1.tip = {weapon1.tip}, weapon2.tip = {weapon2.tip}")
        print(f"weapon1 == weapon2: {weapon1 == weapon2} (должно быть True, если типы совпадают)")
        
        print(f"weapon1.tip = {weapon1.tip}, weapon3.tip = {weapon3.tip}")
        print(f"weapon1 == weapon3: {weapon1 == weapon3} (должно быть False)")
        
        print(f"weapon1 == 'строка': {weapon1 == 'строка'} (должно быть False)")
    except Exception as e:
        print(f"Ошибка в __eq__: {type(e).__name__}: {e}")
    
    
    print("ТЕСТ 7: Проверка инвариантов после операций")
    
    try:
        test_weapon = Weapon(10, "Обычное", 50, "тест", "Меч", "Тест", 1)
        print("Объект создан корректно")
        
    
        print("Проверка граничных значений твердости:")
        test_weapon.hardness = 1
        print(f"Твердость = 1")
        
        for i in range(3):
            result = test_weapon.attack()
            print(f"Атака {i+1}: {result}")
            print(f"Твердость стала: {test_weapon.hardness}")
            print(f"Статус: {test_weapon.status}")
        
        
        if test_weapon.hardness >= 0:
            print("Твердость не стала отрицательной")
        else:
            print("Твердость стала отрицательной!")
        
        
        print("Проверка repair():")
        test_weapon.repair()
        print(f"После repair: {test_weapon.hardness} (должно быть 100)")
        
        print(f"Проверка приватного атрибута __kolichestvo:")
        print(f"kolichestvo = {test_weapon.kolichestvo}")
        
        try:
            print(f"Попытка прямого доступа: {test_weapon.__kolichestvo}")
        except AttributeError:
            print("Прямой доступ к __kolichestvo невозможен (имя искажено)")
        
    except Exception as e:
        print(f"Ошибка при проверке инвариантов: {type(e).__name__}: {e}")


print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
