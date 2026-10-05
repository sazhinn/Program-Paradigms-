# Вариант 1: сумма квадратов положительных чисел (процедурный стиль)
def is_positive(number: int) -> bool:
    return number > 0


def square(number: int) -> int:
    return number ** 2


def sum_positive_squares(values: list[int]) -> int:
    total = 0
    for number in values:
        if is_positive(number):
            total += square(number)
    return total


numbers = [-3, 5, -1, 8, 0, 2, -7, 4]
print("Сумма квадратов положительных:", sum_positive_squares(numbers))
