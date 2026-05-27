"""Собственные исключения для предметной области."""


class ItemNotFoundError(Exception):
    """Объект не найден в коллекции."""
    pass


class DuplicateItemError(Exception):
    """Объект с таким идентификатором уже существует."""
    pass


class InvalidWeaponDataError(Exception):
    """Некорректные данные при создании оружия."""
    pass


class CollectionError(Exception):
    """Ошибка при работе с коллекцией."""
    pass