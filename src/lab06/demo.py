from typing import List
from model import Weapon
from base import Firearms, Edged
from container import TypedCollection, Displayable, Scorable, D, S


def print_separator(title: str) -> None:
    """Печатает разделитель с заголовком"""
    print(f"  {title}")


def demo_displayable_protocol() -> None:
    """
    Демонстрация Protocol Displayable.
    Классы Weapon, Firearms, Edged НЕ наследуются от Displayable,
    но подходят под протокол, так как у всех есть метод display().
    """
    print_separator("ДЕМОНСТРАЦИЯ ПРОТОКОЛА DISPLAYABLE")
    
    # Коллекция с ограничением на Displayable
    displayable_items: TypedCollection[D] = TypedCollection()
    
    # Создаем объекты 
    ilona_sword = Edged(
        damage=85, rare="Легендарное", hardness=100,
        effects="молния, огонь", tip="Двуручный меч", imia="Илона",
        kolichestvo=1, blade_length=95.0, material="хз"
    )
    
    injgraf_gun = Firearms(
        damage=75, rare="Эпическое", hardness=95,
        effects="взрывные, зажигательные", tip="Пулемет", imia="Инжграф",
        kolichestvo=1, caliber=12.7, magazine_capacity=100
    )
    
    nikolai_dagger = Edged(
        damage=45, rare="Редкое", hardness=90,
        effects="яд, кровотечение", tip="Кинжал", imia="Николай Галаев",
        kolichestvo=3, blade_length=32.0, material="давлат"
    )
    
    # Добавляем в коллекцию (все имеют метод display!)
    displayable_items.add(ilona_sword)
    displayable_items.add(injgraf_gun)
    displayable_items.add(nikolai_dagger)
    
    print("Коллекция Displayable объектов:")
    print(f"   Размер: {displayable_items.size()}")
    print("\n   Вызов display() для каждого объекта:")
    
    for item in displayable_items.get_all():
        print(f"      {item.display()}")


def demo_scorable_protocol() -> None:
    """
    Демонстрация Protocol Scorable.
    Классы Weapon, Firearms, Edged имеют метод score(),
    поэтому автоматически соответствуют протоколу.
    """
    print_separator("ДЕМОНСТРАЦИЯ ПРОТОКОЛА SCORABLE")
    
    # Коллекция с ограничением на Scorable
    scorable_items: TypedCollection[S] = TypedCollection()
    
    # Создаем объекты с именами Илона, Инжграф и Николай Галаев
    ilona_legendary = Edged(
        damage=100, rare="Легендарное", hardness=100,
        effects="гром, молния, буря", tip="Грейтсворд", imia="Илона",
        kolichestvo=1, blade_length=120.0, material="хз"
    )
    
    injgraf_rifle = Firearms(
        damage=60, rare="Эпическое", hardness=88,
        effects="точность, пробитие", tip="Снайперская винтовка", imia="Инжграф",
        kolichestvo=2, caliber=8.6, magazine_capacity=10
    )
    
    nikolai_axe = Edged(
        damage=55, rare="Редкое", hardness=85,
        effects="кровотечение", tip="Боевой топор", imia="Николай Галаев",
        kolichestvo=2, blade_length=65.0, material="давлат"
    )
    
    # Добавляем в коллекцию
    scorable_items.add(ilona_legendary)
    scorable_items.add(injgraf_rifle)
    scorable_items.add(nikolai_axe)
    
    print("Коллекция Scorable объектов:")
    print(f"   Размер: {scorable_items.size()}")
    
    print("\n   Оценки (вызов score()):")
    for item in scorable_items.get_all():
        print(f"      {item.display():<55} -> рейтинг: {item.score():.2f}")
    
    # Демонстрация filter с протоколом
    print("\n   [Фильтрация] оружие с рейтингом >= 70:")
    high_rated = scorable_items.filter(lambda x: x.score() >= 70)
    for item in high_rated:
        print(f"      {item.display():<55} -> рейтинг: {item.score():.2f}")
    
    # Демонстрация map с протоколом
    print("\n   [Map] Рейтинги всех предметов:")
    ratings = scorable_items.map(lambda x: x.score())
    for i, rating in enumerate(ratings, 1):
        print(f"      Предмет {i}: {rating:.2f}")


def demo_generic_methods() -> None:
    """Демонстрация работы find, filter, map с разными типами"""
    print_separator("ДЕМОНСТРАЦИЯ GENERIC МЕТОДОВ")
    
    # Коллекция с разным оружием
    weapons_collection: TypedCollection[Weapon] = TypedCollection()
    
    # Добавляем оружие 
    weapons_collection.add(Edged(
        damage=90, rare="Легендарное", hardness=100,
        effects="молния", tip="Меч", imia="Илона",
        kolichestvo=1, blade_length=95.0, material="хз"
    ))
    
    weapons_collection.add(Firearms(
        damage=70, rare="Эпическое", hardness=92,
        effects="взрывные", tip="Дробовик", imia="Инжграф",
        kolichestvo=2, caliber=12.0, magazine_capacity=8
    ))
    
    weapons_collection.add(Edged(
        damage=40, rare="Обычное", hardness=70,
        effects="нет", tip="Кинжал", imia="Николай Галаев",
        kolichestvo=5, blade_length=28.0, material="давлат"
    ))
    
    weapons_collection.add(Firearms(
        damage=95, rare="Легендарное", hardness=98,
        effects="огненные", tip="Пулемет", imia="Илона",
        kolichestvo=1, caliber=14.5, magazine_capacity=50
    ))
    
    print("Коллекция оружия:")
    for w in weapons_collection.get_all():
        print(f"   - {w._imia}: урон {w._damage}, редкость {w._rare}")
    
    # find - успешный поиск
    print("\n[find] поиск оружия с уроном >= 80")
    found = weapons_collection.find(lambda w: w._damage >= 80)
    if found:
        print(f"   [Найдено] {found._imia} (урон: {found._damage})")
    
    # find - неудачный поиск
    print("\n[find] поиск оружия с уроном >= 200")
    not_found = weapons_collection.find(lambda w: w._damage >= 200)
    print(f"   [Результат] {not_found}")
    
    # filter
    print("\n[filter] оружие с редкостью 'Легендарное'")
    legendary_weapons = weapons_collection.filter(
        lambda w: w._rare.lower() == 'легендарное'
    )
    print(f"   Найдено {len(legendary_weapons)} единиц:")
    for w in legendary_weapons:
        print(f"      - {w._imia} ({w._rare}, урон: {w._damage})")
    
    # map - разные типы результатов
    print("\n[map] получение названий (List[str])")
    names = weapons_collection.map(lambda w: w._imia)
    print(f"   {names}")
    
    print("\n[map] получение урона (List[int])")
    damages = weapons_collection.map(lambda w: w._damage)
    print(f"   {damages}")
    
    print("\n[map] получение информации (List[str])")
    info = weapons_collection.map(lambda w: f"{w._imia} - урон {w._damage}")
    for line in info:
        print(f"   {line}")
    
    print("\n[ИТОГ] Тип результата map() меняется в зависимости от функции!")


def demo_type_safety() -> None:
    """Демонстрация типобезопасности"""
    print_separator("ДЕМОНСТРАЦИЯ ТИПОБЕЗОПАСНОСТИ")
    
    # Коллекция с явным типом Edged
    edged_weapons: TypedCollection[Edged] = TypedCollection()
    
    ilona_sword = Edged(
        damage=85, rare="Легендарное", hardness=100,
        effects="молния", tip="Меч", imia="Илона",
        kolichestvo=1, blade_length=95.0, material="Мифрил"
    )
    
    nikolai_dagger = Edged(
        damage=45, rare="Редкое", hardness=90,
        effects="яд", tip="Кинжал", imia="Николай Галаев",
        kolichestvo=3, blade_length=32.0, material="Дамасская сталь"
    )
    
    # Это работает - Edged подходит
    edged_weapons.add(ilona_sword)
    edged_weapons.add(nikolai_dagger)
    print("[OK] TypedCollection[Edged] принимает Edged")
    print(f"   Добавлено оружие: {edged_weapons.size()} единиц")
    
    
    print("\n[ОШИБКА] TypedCollection[Edged] НЕ принимает Firearms")
    print("   IDE подсветит это до выполнения кода!")


def main() -> None:
    """Главная функция"""
    print("Лабораторная работа N6: Типизация в Python")
    print("Демонстрация работы с Generic, TypeVar и Protocols")
    print("Имена: Илона, Инжграф, Николай Галаев")
    
    demo_displayable_protocol()
    demo_scorable_protocol()
    demo_generic_methods()
    demo_type_safety()
    
    print("  КЛЮЧЕВЫЕ ВЫВОДЫ:")
    print("  1. Протоколы позволяют использовать структурную типизацию")
    print("  2. TypeVar с bound= ограничивает тип объектов в коллекции")
    print("  3. Generic классы работают с разными типами без дублирования кода")
    print("  4. IDE проверяет типы и подсказывает доступные методы")



if __name__ == "__main__":
    main()