# Задание 3. Объектно-ориентированный стиль
class NumberCollection:
    def __init__(self, numbers):
        # _numbers - внутренние данные объекта (инкапсуляция),
        # снаружи к ним обращаются только через методы
        self._numbers = list(numbers)

    def get_even_numbers(self):
        return [n for n in self._numbers if n % 2 == 0]

    def count_even_numbers(self):
        return len(self.get_even_numbers())

    def sum_even_squares(self):
        total = 0
        for number in self._numbers:
            if number % 2 == 0:
                total += number ** 2
        return total

    def find_maximum(self):
        return max(self._numbers)

    def calculate_average(self):
        return sum(self._numbers) / len(self._numbers)


collection = NumberCollection([4, 7, 2, 9, 12, 5, 8, 3])
print(collection.get_even_numbers())
print(collection.count_even_numbers())
print(collection.sum_even_squares())
print(collection.find_maximum())
print(collection.calculate_average())

# второй объект с другим набором чисел
other = NumberCollection([1, 2, 3, 4, 10])
print(other.get_even_numbers())
print(other.sum_even_squares())
