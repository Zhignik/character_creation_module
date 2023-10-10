from math import sqrt

message: str = """Добро пожаловать в самую лучшую программу для вычисления
          квадратного корня из заданного числа"""


def сalculate_square_root(number) -> float:
    """Вычисляет квадратный корень."""
    sqrted: float = sqrt(number)
    return sqrted


def calc(your_number) -> str:
    """Выводит итоговый результат."""
    final_sqrted: float = сalculate_square_root(your_number)
    if your_number <= 0:
        print("Невозможно посчитать")
    if your_number > 0:
        print(f"Мы вычислили квадратный корень из введённого вами числа."
              f"Это будет:{final_sqrted}")


print(message)
calc(25.5)
