import unittest

from result_manager import ResultManager


class TestResultManager(unittest.TestCase):
    def setUp(self):
        self.manager = ResultManager()
        self.manager.add_student("S1", "Rahim")
        self.manager.add_course("CSE101", "Programming", 3)
        self.manager.add_course("MAT101", "Mathematics", 2)

    def test_add_student(self):
        self.assertIn("S1", self.manager.students)
        self.assertEqual(self.manager.students["S1"].name, "Rahim")

    def test_duplicate_student_id_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_student("S1", "Karim")

    def test_add_course(self):
        course = self.manager.courses["CSE101"]
        self.assertEqual(course.title, "Programming")
        self.assertEqual(course.credit, 3)

    def test_enter_valid_mark(self):
        self.manager.enter_mark("S1", "CSE101", 85)
        self.assertEqual(self.manager.students["S1"].marks["CSE101"], 85)

    def test_invalid_mark_rejected(self):
        for mark in (-1, 101):
            with self.subTest(mark=mark):
                with self.assertRaises(ValueError):
                    self.manager.enter_mark("S1", "CSE101", mark)

    def test_mark_for_unknown_student_or_course(self):
        with self.assertRaises(ValueError):
            self.manager.enter_mark("S99", "CSE101", 80)
        with self.assertRaises(ValueError):
            self.manager.enter_mark("S1", "XXX000", 80)

    def test_cgpa_weighted_by_credit(self):
        self.manager.enter_mark("S1", "CSE101", 85)  # A+ 4.00 x 3
        self.manager.enter_mark("S1", "MAT101", 62)  # B  3.00 x 2
        # (4.00*3 + 3.00*2) / 5 = 3.60
        self.assertEqual(self.manager.calculate_cgpa("S1"), 3.60)

    def test_cgpa_with_no_marks(self):
        self.assertEqual(self.manager.calculate_cgpa("S1"), 0.0)

    def test_result_sheet(self):
        self.manager.enter_mark("S1", "CSE101", 72)
        rows, cgpa = self.manager.get_result_sheet("S1")
        self.assertEqual(rows, [("CSE101", "Programming", 3, 72, "A-", 3.50)])
        self.assertEqual(cgpa, 3.50)


if __name__ == "__main__":
    unittest.main()
