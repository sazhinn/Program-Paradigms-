# Задание 2. Процедурный стиль
def is_even(number: int) -> bool:
    return number % 2 == 0


def square(number: int) -> int:
    return number ** 2


def get_even_numbers(values: list[int]) -> list[int]:
    result = []
    for number in values:
        if is_even(number):
            result.append(number)
    return result


def sum_even_squares(values: list[int]) -> int:
    total = 0
    for number in get_even_numbers(values):
        total += square(number)
    return total


numbers = [4, 7, 2, 9, 12, 5, 8, 3]

# отдельные проверки функций
print(is_even(4), is_even(7))
print(square(5))
print(get_even_numbers(numbers))
print(sum_even_squares(numbers))
