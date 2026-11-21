GRADE_SCALE = [
    (80, "A+", 4.00),
    (75, "A", 3.75),
    (70, "A-", 3.50),
    (65, "B+", 3.25),
    (60, "B", 3.00),
    (55, "B-", 2.75),
    (50, "C+", 2.50),
    (45, "C", 2.25),
    (40, "D", 2.00),
    (0, "F", 0.00),
]


def get_grade(mark):
    """Return (letter_grade, grade_point) for a mark between 0 and 100."""
    if mark < 0 or mark > 100:
        raise ValueError("Mark must be between 0 and 100.")
    for min_mark, letter, point in GRADE_SCALE:
        if mark >= min_mark:
            return letter, point
