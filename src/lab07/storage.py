"""Модуль для сохранения и загрузки коллекции оружия в/из JSON."""

import json
import os
from typing import List, Dict, Any
from models import Weapon
from collection import Inventory
from base import Firearms, Edged


def _weapon_to_dict(weapon: Weapon) -> Dict[str, Any]:
    """
    Преобразует объект Weapon в словарь для JSON.
    
    Args:
        weapon: объект Weapon или его наследник
        
    Returns:
        Dict[str, Any]: словарь с данными оружия
    """
    data = {
        'type': 'Weapon',
        'imia': weapon._imia,
        'damage': weapon._damage,
        'rare': weapon._rare,
        'hardness': weapon._hardness,
        'effects': weapon._effects,
        'tip': weapon._tip,
        'kolichestvo': weapon._Weapon__kolichestvo  # приватный атрибут
    }
    
    if isinstance(weapon, Firearms):
        data['type'] = 'Firearms'
        data['caliber'] = weapon._caliber
        data['magazine_capacity'] = weapon._magazine_capacity
    elif isinstance(weapon, Edged):
        data['type'] = 'Edged'
        data['blade_length'] = weapon._blade_length
        data['material'] = weapon._material
    
    return data


def _dict_to_weapon(data: Dict[str, Any]) -> Weapon:
    """
    Преобразует словарь обратно в объект Weapon.
    
    Args:
        data: словарь с данными оружия
        
    Returns:
        Weapon: восстановленный объект
    """
    weapon_type = data.get('type', 'Weapon')
    
    if weapon_type == 'Firearms':
        return Firearms(
            damage=data['damage'],
            rare=data['rare'],
            hardness=data['hardness'],
            effects=data['effects'],
            tip=data['tip'],
            imia=data['imia'],
            kolichestvo=data['kolichestvo'],
            caliber=data['caliber'],
            magazine_capacity=data['magazine_capacity']
        )
    elif weapon_type == 'Edged':
        return Edged(
            damage=data['damage'],
            rare=data['rare'],
            hardness=data['hardness'],
            effects=data['effects'],
            tip=data['tip'],
            imia=data['imia'],
            kolichestvo=data['kolichestvo'],
            blade_length=data['blade_length'],
            material=data['material']
        )
    else:
        return Weapon(
            damage=data['damage'],
            rare=data['rare'],
            hardness=data['hardness'],
            effects=data['effects'],
            tip=data['tip'],
            imia=data['imia'],
            kolichestvo=data['kolichestvo']
        )


def save(collection: Inventory, filepath: str) -> None:
    """
    Сохранить коллекцию в JSON-файл.
    
    Args:
        collection: объект Inventory с оружием
        filepath: путь к файлу для сохранения
    """
    items_data = [_weapon_to_dict(item) for item in collection.items]
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(items_data, f, ensure_ascii=False, indent=2)
    print(f"Сохранено {len(items_data)} предметов в {filepath}")


def load(filepath: str) -> Inventory:
    """
    Загрузить объекты из JSON-файла.
    
    Args:
        filepath: путь к файлу для загрузки
        
    Returns:
        Inventory: загруженная коллекция
    """
    inventory = Inventory()
    
    if not os.path.exists(filepath):
        print(f"Файл {filepath} не найден, создана пустая коллекция")
        return inventory
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            items_data = json.load(f)
        
        for item_data in items_data:
            try:
                weapon = _dict_to_weapon(item_data)
                # Используем прямой доступ к _items из-за бага в Inventory.add()
                if weapon not in inventory._items:
                    # Проверка на дубликат по имени
                    existing_names = [w._imia for w in inventory._items]
                    if weapon._imia not in existing_names:
                        inventory._items.append(weapon)
            except Exception as e:
                print(f"Ошибка загрузки предмета: {e}")
        
        print(f"Загружено {len(inventory._items)} предметов из {filepath}")
        
    except json.JSONDecodeError as e:
        print(f"Ошибка чтения JSON: {e}")
    except Exception as e:
        print(f"Ошибка загрузки: {e}")
    
    return inventory