class StudentMarkManager:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def add_student(self, student):
        self.__students.append(student)

    def add_course(self, course):
        self.__courses.append(course)

    def input_marks_for_courses(self):
        self.list_courses()
        course_id = input("Select a course ID to input marks: ")
        for student in self.__students:
            mark = float(input(f"Enter marks for {student} in course {course_id}: "))
            student.set_mark(course_id, mark)

    def calculate_gpa_for_all_students(self):
        for student in self.__students:
            student.calculate_gpa(self.__courses)

    def list_courses(self):
        print("Courses List:")
        for course in self.__courses:
            print(course)

    def list_students(self):
        print("Students List:")
        for student in self.__students:
            print(student)

    def show_student_marks(self):
        self.list_courses()
        course_id = input("Enter course ID to show student marks: ")
        print(f"Marks for course {course_id}:")
        for student in self.__students:
            mark = student.get_mark(course_id)
            if mark is not None:
                print(f"{student} -> Marks: {mark}")
            else:
                print(f"{student} -> Marks: No marks recorded")

    def sort_students_by_gpa(self):
        self.__students.sort(key=lambda student: student.get_gpa(), reverse=True)
