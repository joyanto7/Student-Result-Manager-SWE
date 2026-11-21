from result_manager import ResultManager


def show_result_sheet(manager, student_id):
    rows, cgpa = manager.get_result_sheet(student_id)
    student = manager.students[student_id]
    print(f"\nResult Sheet - {student.name} ({student.student_id})")
    print(f"{'Code':<10}{'Title':<25}{'Credit':<8}{'Mark':<7}{'Grade':<7}{'Point'}")
    for code, title, credit, mark, grade, point in rows:
        print(f"{code:<10}{title:<25}{credit:<8}{mark:<7}{grade:<7}{point:.2f}")
    print(f"CGPA: {cgpa:.2f}\n")


def main():
    manager = ResultManager()

    while True:
        print("1. Add Student")
        print("2. Add Course")
        print("3. Enter Marks")
        print("4. Show Result Sheet")
        print("0. Exit")
        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                student_id = input("Student ID: ").strip()
                name = input("Name: ").strip()
                manager.add_student(student_id, name)
                print("Student added.\n")

            elif choice == "2":
                code = input("Course code: ").strip()
                title = input("Course title: ").strip()
                credit = float(input("Credit: "))
                manager.add_course(code, title, credit)
                print("Course added.\n")

            elif choice == "3":
                student_id = input("Student ID: ").strip()
                code = input("Course code: ").strip()
                mark = float(input("Mark (0-100): "))
                manager.enter_mark(student_id, code, mark)
                print("Mark saved.\n")

            elif choice == "4":
                student_id = input("Student ID: ").strip()
                show_result_sheet(manager, student_id)

            elif choice == "0":
                break

            else:
                print("Invalid choice.\n")

        except ValueError as error:
            print(f"Error: {error}\n")


if __name__ == "__main__":
    main()
