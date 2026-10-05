import os
import sys
import unittest
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from attendance import AttendanceJournal, StudentAttendance  # noqa: E402


class AttendanceTests(unittest.TestCase):
    def test_rate_and_status_pass(self):
        s = StudentAttendance(1, "Amina")
        for d in (1, 2, 3):
            s.mark_present(date(2026, 10, d))
        s.mark_absent(date(2026, 10, 4))
        self.assertEqual(s.attendance_rate, 75)
        self.assertEqual(s.status, "допущен")

    def test_status_fail(self):
        s = StudentAttendance(1, "Dias")
        s.mark_present(date(2026, 10, 1))
        s.mark_absent(date(2026, 10, 2))
        self.assertEqual(s.status, "не допущен")

    def test_no_data(self):
        s = StudentAttendance(1, "Mira")
        self.assertIsNone(s.attendance_rate)
        self.assertEqual(s.status, "нет данных")

    def test_excused_does_not_reduce_rate(self):
        s = StudentAttendance(1, "Amina")
        s.mark_present(date(2026, 10, 1))
        s.mark_absent(date(2026, 10, 2), excused=True)
        self.assertEqual(s.attendance_rate, 100)

    def test_snapshot_is_tuple(self):
        s = StudentAttendance(1, "Amina")
        s.mark_present(date(2026, 10, 1))
        self.assertIsInstance(s.present_dates, tuple)

    def test_error_duplicate_date(self):
        s = StudentAttendance(1, "Amina")
        s.mark_present(date(2026, 10, 1))
        with self.assertRaises(ValueError):
            s.mark_absent(date(2026, 10, 1))
        self.assertEqual(s.absent_dates, ())  # состояние не изменилось

    def test_error_bad_date_type(self):
        s = StudentAttendance(1, "Amina")
        with self.assertRaises(TypeError):
            s.mark_present("2026-10-01")

    def test_error_bad_id_and_name(self):
        with self.assertRaises(ValueError):
            StudentAttendance(0, "A")
        with self.assertRaises(ValueError):
            StudentAttendance(1, "  ")

    def test_journal_duplicate_and_unknown(self):
        j = AttendanceJournal()
        j.register(StudentAttendance(1, "Amina"))
        with self.assertRaises(ValueError):
            j.register(StudentAttendance(1, "Other"))
        with self.assertRaises(KeyError):
            j.mark_present(99, date(2026, 10, 1))

    def test_journal_report_order(self):
        j = AttendanceJournal()
        j.register(StudentAttendance(1, "NoData"))
        j.register(StudentAttendance(2, "Low"))
        j.register(StudentAttendance(3, "High"))
        j.mark_present(3, date(2026, 10, 1))
        j.mark_absent(2, date(2026, 10, 1))
        names = [s.name for s in j.report()]
        self.assertEqual(names, ["High", "Low", "NoData"])


if __name__ == "__main__":
    unittest.main()
