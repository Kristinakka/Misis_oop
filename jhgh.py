# нет родителя
class Sword:
    def attack(target):
        print("Удар по" + target.name)

# независимый класс, но имеет тот же метод
class Bow:
    def attack(target):
        print("Стреляем в " + target.name)

# функция ждет любой объект с методом attack(target)
def use_weapon(weapon, target):
    weapon.attack(target)  

# Пример использования
erfuehyu = Sword()
dcdie = Bow()

print(use_weapon(Sword))   
print(use_weapon(Bow))   