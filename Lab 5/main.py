from datetime import date

from attendance import AttendanceJournal, StudentAttendance


def main():
    journal = AttendanceJournal()
    journal.register(StudentAttendance(1, "Amina"))
    journal.register(StudentAttendance(2, "Dias"))
    journal.register(StudentAttendance(3, "Mira"))

    # Amina: 4 присутствия, 1 неуважительный пропуск -> 80%
    for day in (1, 2, 3, 4):
        journal.mark_present(1, date(2026, 10, day))
    journal.mark_absent(1, date(2026, 10, 5))

    # Dias: 2 присутствия, 2 пропуска, один уважительный -> 2 из 3 = 66.67%
    journal.mark_present(2, date(2026, 10, 1))
    journal.mark_present(2, date(2026, 10, 2))
    journal.mark_absent(2, date(2026, 10, 3))
    journal.mark_absent(2, date(2026, 10, 4), excused=True)

    for student in journal.report():
        rate = student.attendance_rate
        text = "-" if rate is None else f"{rate:.2f}%"
        print(f"{student.name}: {text}; {student.status}")


if __name__ == "__main__":
    main()
