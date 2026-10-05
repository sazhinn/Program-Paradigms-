# Вариант 1: сумма квадратов положительных чисел (императивный стиль)
numbers = [-3, 5, -1, 8, 0, 2, -7, 4]

total = 0
for number in numbers:
    if number > 0:
        total += number ** 2

print("Сумма квадратов положительных:", total)
