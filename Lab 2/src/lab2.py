# Лабораторная работа 2. Императивная парадигма
# Индивидуальный вариант 1: банковский счет


def task1_state():
    print("=== Задание 1. Изменение состояния ===")
    x = 10
    print("1) x = 10     ->", x)
    x = x + 5
    print("2) x = x + 5  ->", x)
    x = x * 2
    print("3) x = x * 2  ->", x)
    x = x - 8
    print("4) x = x - 8  ->", x)
    x = x // 2
    print("5) x = x // 2 ->", x)
    print("Результат:", x)
    print()


def task2_purchase():
    print("=== Задание 2. Стоимость покупки ===")
    price = float(input("Цена товара: "))
    quantity = int(input("Количество: "))
    discount_percent = float(input("Скидка (%): "))

    total = price * quantity
    discount = total * discount_percent / 100
    to_pay = total - discount

    print("Стоимость без скидки:", total)
    print("Размер скидки:", discount)
    print("К оплате:", to_pay)
    print()


def task3_grade():
    print("=== Задание 3. Оценка по баллам ===")
    score = int(input("Введите балл (0-100): "))

    if score < 0 or score > 100:
        print("Ошибка: балл должен быть от 0 до 100")
    elif score >= 90:
        print("Оценка: A")
    elif score >= 75:
        print("Оценка: B")
    elif score >= 50:
        print("Оценка: C")
    else:
        print("Оценка: F")
    print()


def task4_accumulation():
    print("=== Задание 4. Накопление состояния в цикле ===")
    numbers = [12, -5, 8, -3, 21, 0, 14, -7]

    total = 0
    positive_sum = 0
    positive_count = 0
    negative_count = 0
    zero_count = 0

    for number in numbers:
        total = total + number
        if number > 0:
            positive_sum = positive_sum + number
            positive_count = positive_count + 1
        elif number < 0:
            negative_count = negative_count + 1
        else:
            zero_count = zero_count + 1
        # состояние после каждой итерации
        print(f"число={number:3}  total={total:3}  positive_sum={positive_sum:3}")

    print("Сумма всех:", total)
    print("Сумма положительных:", positive_sum)
    print("Положительных:", positive_count)
    print("Отрицательных:", negative_count)
    print("Нулей:", zero_count)
    print()


def task5_maximum():
    print("=== Задание 5. Поиск максимума ===")
    scores = [67, 82, 45, 91, 76, 88, 54]
    maximum = scores[0]

    for score in scores:
        before = maximum
        if score > maximum:
            maximum = score
        print(f"score={score}  maximum до={before}  score>maximum={score > before}  maximum после={maximum}")

    print("Максимум:", maximum)
    print()


def variant1_bank():
    print("=== Индивидуальный вариант 1. Банковский счет ===")
    balance = float(input("Баланс на счете: "))
    amount = float(input("Сумма снятия: "))

    if amount <= 0:
        print("Ошибка: сумма должна быть больше нуля")
    elif amount <= balance:
        balance = balance - amount  # состояние меняется только при достаточных средствах
        print("Снятие выполнено. Новый баланс:", balance)
    else:
        print("Недостаточно средств. Баланс не изменился:", balance)
    print()


def comparison():
    print("=== Сравнительное задание ===")
    numbers = [-4, 7, -2, 10, 5, -8]

    # императивный стиль
    total = 0
    for number in numbers:
        if number > 0:
            total = total + number
    print("Императивно:", total)

    # декларативный стиль
    total = sum(number for number in numbers if number > 0)
    print("Декларативно:", total)
    print()


task1_state()
task2_purchase()
task3_grade()
task4_accumulation()
task5_maximum()
variant1_bank()
comparison()
