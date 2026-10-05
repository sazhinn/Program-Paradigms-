import unittest

from university_rating.calculations import (
    calculate_average, determine_letter, determine_status,
)
from university_rating.rating import build_rating
from university_rating.validation import validate_scores, validate_student


class RatingTests(unittest.TestCase):
    def test_empty_average(self):
        self.assertIsNone(calculate_average([]))

    def test_status_boundary(self):
        self.assertEqual(determine_status(49.99), "не допущен")
        self.assertEqual(determine_status(50), "допущен")
        self.assertEqual(determine_status(None), "нет данных")

    def test_invalid_score(self):
        with self.assertRaises(ValueError):
            validate_scores([80, 101])

    def test_wrong_type_score(self):
        with self.assertRaises(TypeError):
            validate_scores(["80"])
        with self.assertRaises(TypeError):
            validate_scores([True])

    def test_border_scores_allowed(self):
        self.assertEqual(validate_scores([0, 100]), [0.0, 100.0])

    def test_missing_name(self):
        with self.assertRaises(ValueError) as ctx:
            validate_student({"id": 1, "scores": [50]})
        self.assertIn("name", str(ctx.exception))

    def test_empty_students(self):
        self.assertEqual(build_rating([]), [])

    def test_no_scores_last(self):
        students = [
            {"id": 1, "name": "A", "scores": []},
            {"id": 2, "name": "B", "scores": [10]},
        ]
        rating = build_rating(students)
        self.assertEqual(rating[0]["name"], "B")
        self.assertIsNone(rating[1]["average"])

    def test_equal_average_is_stable(self):
        students = [
            {"id": 1, "name": "A", "scores": [70]},
            {"id": 2, "name": "B", "scores": [70]},
        ]
        first = build_rating(students)
        second = build_rating(students)
        self.assertEqual(first, second)

    def test_source_is_not_changed(self):
        students = [{"id": 1, "name": "Test", "scores": [70, 80]}]
        before = [{"id": 1, "name": "Test", "scores": [70, 80]}]
        build_rating(students)
        self.assertEqual(students, before)

    # тесты индивидуального расширения (вариант 1, буквенная оценка)
    def test_letter_boundaries(self):
        self.assertEqual(determine_letter(90), "A")
        self.assertEqual(determine_letter(89.99), "B")
        self.assertEqual(determine_letter(75), "B")
        self.assertEqual(determine_letter(60), "C")
        self.assertEqual(determine_letter(50), "D")
        self.assertEqual(determine_letter(49.99), "F")

    def test_letter_none_and_in_rating(self):
        self.assertIsNone(determine_letter(None))
        rating = build_rating([{"id": 1, "name": "X", "scores": [95, 91]}])
        self.assertEqual(rating[0]["letter"], "A")


if __name__ == "__main__":
    unittest.main()
