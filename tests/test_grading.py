import unittest

from grading import get_grade


class TestGrading(unittest.TestCase):
    def test_grade_boundaries(self):
        cases = [
            (100, "A+", 4.00), (80, "A+", 4.00),
            (79, "A", 3.75), (75, "A", 3.75),
            (74, "A-", 3.50), (70, "A-", 3.50),
            (69, "B+", 3.25), (65, "B+", 3.25),
            (64, "B", 3.00), (60, "B", 3.00),
            (59, "B-", 2.75), (55, "B-", 2.75),
            (54, "C+", 2.50), (50, "C+", 2.50),
            (49, "C", 2.25), (45, "C", 2.25),
            (44, "D", 2.00), (40, "D", 2.00),
            (39, "F", 0.00), (0, "F", 0.00),
        ]
        for mark, grade, point in cases:
            with self.subTest(mark=mark):
                self.assertEqual(get_grade(mark), (grade, point))

    def test_invalid_marks(self):
        for mark in (-1, 101):
            with self.subTest(mark=mark):
                with self.assertRaises(ValueError):
                    get_grade(mark)


if __name__ == "__main__":
    unittest.main()
