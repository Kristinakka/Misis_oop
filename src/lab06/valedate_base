def validate_caliber(caliber):
    if isinstance(caliber, (int, float)):
        if 1.0 <= caliber <= 50.0:
            return caliber
        raise ValueError("Калибр должен быть в диапазоне от 1.0 до 50.0 мм")
    raise ValueError("Калибр должен быть числом")

def validate_magazine_capacity(magazine_capacity):
    if isinstance(magazine_capacity, int):
        if 1 <= magazine_capacity <= 100:
            return magazine_capacity
        raise ValueError("Емкость магазина должна быть целым числом от 1 до 100")
    raise ValueError("Емкость магазина должна быть целым числом")

def validate_blade_length(blade_length):
    if isinstance(blade_length, (int, float)):
        if 5.0 <= blade_length <= 200.0:
            return blade_length
        raise ValueError("Длина клинка должна быть в диапазоне от 5.0 до 200.0 см")
    raise ValueError("Длина клинка должна быть числом")

def validate_material(material):
    valid_materials = ["сталь", "титан", "булат", "давлат", "хз", "кдчд"]
    if material in valid_materials:
        return material
    raise ValueError(f"Материал должен быть одним из: {valid_materials}")