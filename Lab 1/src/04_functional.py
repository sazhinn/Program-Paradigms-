# Задание 4. Функциональный стиль
numbers = [4, 7, 2, 9, 12, 5, 8, 3]

# filter + map + sum
result = sum(
    map(
        lambda number: number ** 2,
        filter(lambda number: number % 2 == 0, numbers)
    )
)
print(result)

# то же генераторным выражением
result_gen = sum(n ** 2 for n in numbers if n % 2 == 0)
print(result_gen)

# отдельный список квадратов чётных чисел
squares = [n ** 2 for n in numbers if n % 2 == 0]
print(squares)

# Изменяемых переменных нет, в императивной версии их 4 (total, even_numbers, squares, iterations)
