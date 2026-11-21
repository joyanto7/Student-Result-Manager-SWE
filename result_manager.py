from models import Student, Course
from grading import get_grade


class ResultManager:
    def __init__(self):
        self.students = {}  # student_id -> Student
        self.courses = {}   # course_code -> Course

    def add_student(self, student_id, name):
        if student_id in self.students:
            raise ValueError(f"Student ID {student_id} already exists.")
        self.students[student_id] = Student(student_id, name)

    def add_course(self, code, title, credit):
        if code in self.courses:
            raise ValueError(f"Course {code} already exists.")
        if credit <= 0:
            raise ValueError("Credit must be greater than 0.")
        self.courses[code] = Course(code, title, credit)

    def enter_mark(self, student_id, course_code, mark):
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} not found.")
        if course_code not in self.courses:
            raise ValueError(f"Course {course_code} not found.")
        if mark < 0 or mark > 100:
            raise ValueError("Mark must be between 0 and 100.")
        self.students[student_id].add_mark(course_code, mark)

    def calculate_cgpa(self, student_id):
        student = self.students[student_id]
        total_points = 0
        total_credits = 0
        for course_code, mark in student.marks.items():
            credit = self.courses[course_code].credit
            _, point = get_grade(mark)
            total_points += point * credit
            total_credits += credit
        if total_credits == 0:
            return 0.0
        return round(total_points / total_credits, 2)

    def get_result_sheet(self, student_id):
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} not found.")
        student = self.students[student_id]
        rows = []
        for course_code, mark in student.marks.items():
            course = self.courses[course_code]
            grade, point = get_grade(mark)
            rows.append((course.code, course.title, course.credit, mark, grade, point))
        return rows, self.calculate_cgpa(student_id)
