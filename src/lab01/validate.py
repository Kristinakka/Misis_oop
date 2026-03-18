def validate_imia(imia):
    if isinstance(imia, str) and imia != '':
        return imia
    else:
        raise TypeError('Неверный тип названия.')
    

def validate_damage(damage):
    if isinstance(damage, int) and damage > 0:
        return damage
    else:                                              
        raise TypeError('Неверный формат урона оружия.')
    

def validate_tip(tip):
    if tip in ['Нож', 'Дубинка', 'Меч', 'Топор', 'Копье', 'Лук', 'Арбалет', 'Кувалда', 'Щит','Пушка']:
        return tip
    else:
        raise TypeError('Неверный тип оружия.')
    

def validate_effects(effects):
    if isinstance(effects, str):
        return effects
    else:
        raise TypeError('Неверный тип эффектов оружия.')
    

def validate_rare(rare):
    if rare in ['Обычное', 'Редкое', 'Сверхредкое' , 'Эпическое' , 'Мифическое' , 'Легендарное']:
        return rare
    else:
        raise TypeError('Неверный формат редоксти оружия')
    

def validate_hardness(hardness):
    if isinstance(hardness, int) and hardness >= 0 and hardness <= 100: #защищенный тип данных
        return hardness
    else:
        raise TypeError('Неверный тип прочности оружия')
        

def validate_kolichestvo(kolichestvo):
    if isinstance(kolichestvo, int) and kolichestvo >= 0: #полностью приватный метод
        return kolichestvo
    else:
        raise TypeError('Неверный формат количества обладателей данным оружием')
        
