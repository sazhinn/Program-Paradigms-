# Вариант 1: сумма квадратов положительных чисел (функциональный стиль)
numbers = [-3, 5, -1, 8, 0, 2, -7, 4]

result = sum(map(lambda n: n ** 2, filter(lambda n: n > 0, numbers)))
print("Сумма квадратов положительных:", result)
