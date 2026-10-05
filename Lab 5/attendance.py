"""Вариант 1. Учет посещаемости: StudentAttendance и AttendanceJournal."""
from datetime import date

PASSING_RATE = 70  # порог допуска, %


class StudentAttendance:
    """Посещаемость одного студента.

    Инварианты: id > 0, имя не пустое, на одну дату только одна отметка.
    """

    def __init__(self, student_id, name):
        if isinstance(student_id, bool) or not isinstance(student_id, int):
            raise TypeError("Идентификатор должен быть целым числом")
        if student_id <= 0:
            raise ValueError("Идентификатор должен быть положительным")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Имя не должно быть пустым")

        self.student_id = student_id
        self.name = name.strip()
        # дата -> "present" / "absent" / "excused"
        self._records = {}

    def _check_new_date(self, day):
        if not isinstance(day, date):
            raise TypeError("Дата должна быть объектом datetime.date")
        if day in self._records:
            raise ValueError(f"Отметка на {day} уже есть")

    def mark_present(self, day):
        """Отмечает присутствие на дату."""
        self._check_new_date(day)
        self._records[day] = "present"

    def mark_absent(self, day, excused=False):
        """Отмечает пропуск. Уважительный пропуск не снижает процент."""
        self._check_new_date(day)
        self._records[day] = "excused" if excused else "absent"

    def _dates(self, kind):
        return tuple(sorted(d for d, k in self._records.items() if k == kind))

    @property
    def present_dates(self):
        """Неизменяемый снимок дат присутствия."""
        return self._dates("present")

    @property
    def absent_dates(self):
        """Неизменяемый снимок дат неуважительных пропусков."""
        return self._dates("absent")

    @property
    def excused_dates(self):
        """Неизменяемый снимок дат уважительных пропусков."""
        return self._dates("excused")

    @property
    def attendance_rate(self):
        """Процент посещаемости или None, если нет учитываемых занятий."""
        present = len(self.present_dates)
        counted = present + len(self.absent_dates)  # уважительные не считаем
        if counted == 0:
            return None
        return present / counted * 100

    @property
    def status(self):
        """Статус допуска по порогу 70%."""
        rate = self.attendance_rate
        if rate is None:
            return "нет данных"
        return "допущен" if rate >= PASSING_RATE else "не допущен"

    def __repr__(self):
        return f"StudentAttendance(student_id={self.student_id!r}, name={self.name!r})"


class AttendanceJournal:
    """Журнал посещаемости: регистрация студентов и делегирование отметок."""

    def __init__(self):
        self._students = {}

    def register(self, student):
        """Регистрирует студента, идентификатор должен быть уникальным."""
        if not isinstance(student, StudentAttendance):
            raise TypeError("Ожидается объект StudentAttendance")
        if student.student_id in self._students:
            raise ValueError("Студент уже зарегистрирован")
        self._students[student.student_id] = student

    def _get(self, student_id):
        try:
            return self._students[student_id]
        except KeyError as error:
            raise KeyError("Студент не найден") from error

    def mark_present(self, student_id, day):
        """Отмечает присутствие студента."""
        self._get(student_id).mark_present(day)

    def mark_absent(self, student_id, day, excused=False):
        """Отмечает пропуск студента."""
        self._get(student_id).mark_absent(day, excused)

    def find(self, student_id):
        """Возвращает студента или None."""
        return self._students.get(student_id)

    def report(self):
        """Студенты по убыванию посещаемости, без данных в конце."""
        return tuple(sorted(
            self._students.values(),
            key=lambda s: (s.attendance_rate is not None, s.attendance_rate or 0),
            reverse=True,
        ))
