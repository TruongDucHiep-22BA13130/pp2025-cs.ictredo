import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}

    def set_mark(self, course_id, mark):
        self.__marks[course_id] = math.floor(mark * 10) / 10

    def get_mark(self, course_id):
        return self.__marks.get(course_id, None)

    def __str__(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, DoB: {self.__dob}"

    def list_marks(self):
        return self.__marks

    def calculate_gpa(self, course_credits):
        total_marks = 0
        total_credits = 0
        for course_id, mark in self.__marks.items():
            if course_id in course_credits:
                total_marks += mark * course_credits[course_id]
                total_credits += course_credits[course_id]
        return total_marks / total_credits if total_credits > 0 else 0


class Course:
    def __init__(self, course_id, name, credits):
        self.__course_id = course_id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__course_id

    def get_credits(self):
        return self.__credits

    def __str__(self):
        return f"Course ID: {self.__course_id}, Name: {self.__name}, Credits: {self.__credits}"


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
            credits = int(input("Enter course credits: "))
            course = Course(course_id, name, credits)
            self.__courses.append(course)

    def input_marks_for_courses(self):
        course_credits = {course.get_id(): course.get_credits() for course in self.__courses}
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

    def calculate_and_sort_gpa(self):
        course_credits = {course.get_id(): course.get_credits() for course in self.__courses}
        student_gpa = [(student, student.calculate_gpa(course_credits)) for student in self.__students]
        sorted_students = sorted(student_gpa, key=lambda x: x[1], reverse=True)
        return sorted_students


def main(stdscr):
   
    curses.curs_set(0)  
    student_mark_manager = StudentMarkManager()

    student_mark_manager.input_number_of_students()
    student_mark_manager.input_number_of_courses()
    student_mark_manager.input_marks_for_courses()

    stdscr.clear()
    stdscr.addstr(0, 0, "List of Students and Marks:")
    stdscr.addstr(1, 0, "-" * 30)
    student_mark_manager.list_students()
    student_mark_manager.show_student_marks()

    sorted_students = student_mark_manager.calculate_and_sort_gpa()

    stdscr.addstr(3, 0, "Sorted Students by GPA:")
    stdscr.addstr(4, 0, "-" * 30)
    for idx, (student, gpa) in enumerate(sorted_students):
        stdscr.addstr(5 + idx, 0, f"{student} -> GPA: {gpa:.2f}")

    stdscr.refresh()
    stdscr.getch()  


if __name__ == "__main__":
    curses.wrapper(main)