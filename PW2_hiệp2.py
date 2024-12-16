class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}

    def set_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def get_mark(self, course_id):
        return self.__marks.get(course_id, None)

    def __str__(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, DoB: {self.__dob}"

    def list_marks(self):
        return self.__marks


class Course:
    def __init__(self, course_id, name):
        self.__course_id = course_id
        self.__name = name

    def __str__(self):
        return f"Course ID: {self.__course_id}, Name: {self.__name}"


class StudentMarkManager:
    def __init__(self):
        self.__students = []
        self.__courses = []

    def input_number_of_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
            student = Student(student_id, name, dob)
            self.__students.append(student)

    def input_number_of_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            course = Course(course_id, name)
            self.__courses.append(course)

    def input_marks_for_courses(self):
        self.list_courses()
        course_id = input("Select a course ID to input marks: ")
        for student in self.__students:
            mark = float(input(f"Enter marks for {student} in course {course_id}: "))
            student.set_mark(course_id, mark)

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



student_mark_manager = StudentMarkManager()

student_mark_manager.input_number_of_students()
student_mark_manager.input_number_of_courses()
student_mark_manager.input_marks_for_courses()

student_mark_manager.list_students()
student_mark_manager.show_student_marks()