class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.marks = {}  # course_code -> mark

    def add_mark(self, course_code, mark):
        self.marks[course_code] = mark


class Course:
    def __init__(self, code, title, credit):
        self.code = code
        self.title = title
        self.credit = credit
