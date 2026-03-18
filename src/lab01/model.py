from validate import * 

class Weapon:
    def __init__(self, damage, rare, hardness, effects, tip, imia, kolichestvo):
        # Используем защищенные атрибуты для хранения значений
        self._imia = validate_imia(imia) 
        self._damage = validate_damage(damage)
        self._tip = validate_tip(tip)
        self._effects = validate_effects(effects)
        self._rare = validate_rare(rare)
        self._hardness = validate_hardness(hardness)
        self.__kolichestvo = validate_kolichestvo(kolichestvo)


    @property
    def rename(self):
        return self._imia
    
    @rename.setter
    def rename(self, new_name):
        if isinstance(new_name, str) and new_name != '':
            self._imia = new_name
        else:
            raise TypeError('Неверный формат названия оружия.')


    @property
    def status(self):
        if self._hardness > 0:
            return 'Состояние: Не сломано'
        else:
            return 'Состояние: Сломано'


    #ОСНОВНЫЕ МЕТОДЫ КЛАССА
    def __str__(self):
        if self._hardness > 0:
            return f'Вот краткая информация по вашему оружию! Название: {self._imia}, тип: {self._tip}, эффекты: {self._effects}, редкость: {self._rare}, урон: {self._damage}'
        else:
            return f'Ваше оружие сломано! Вот его характеристики: Название: {self._imia}, тип: {self._tip}, эффекты: {self._effects}, редкость: {self._rare}, урон: {self._damage}'

    def attack(self):
        if self._hardness == 0:
            return 'Ваше оружие сломано и не наносит урон противнику.'
        else:
            self._hardness -= 1
            return f'Вы попали по противнику и нанесли {self._damage} урона.' 

    def __repr__(self):
        return f'Вся информация по экземпляру. Название: {self._imia}, тип: {self._tip}, эффекты: {self._effects}, твердость: {self._hardness}, редкость: {self._rare}, урон: {self._damage}, количество пользователей: {self.__kolichestvo}'

    def __eq__(self, other):
        if isinstance(other, Weapon):
            return self._tip == other._tip
        return False
    
    def repair(self):
        if self._hardness < 100:
            self._hardness = 100
            return "Оружие восстановлено!"
        else:
            return "Ваше оружие имеет максимальную прочность!"
