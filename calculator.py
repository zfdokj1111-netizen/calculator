# calculator.py


def add(a: float, b: float) -> float:
    """Возвращает сумму двух чисел"""
    return a + b


def subtract(a: float, b: float) -> float:
    """Возвращает разность a - b"""
    return a - b


def multiply(a: float, b: float) -> float:
    """Возвращает произведение"""
    return a * b


def divide(a: float, b: float) -> float:
    """Возвращает результат деления a / b, если b ≠ 0"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b
