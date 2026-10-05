PASSING_AVERAGE = 50


def calculate_average(scores):
    """Возвращает среднее или None для пустой последовательности."""
    return sum(scores) / len(scores) if scores else None


def determine_status(average):
    """Возвращает статус по среднему баллу."""
    if average is None:
        return "нет данных"
    return "допущен" if average >= PASSING_AVERAGE else "не допущен"


def determine_letter(average):
    """Возвращает буквенную оценку A, B, C, D, F или None, если данных нет."""
    if average is None:
        return None
    if average >= 90:
        return "A"
    if average >= 75:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"
