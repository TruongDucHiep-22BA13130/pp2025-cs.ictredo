import math

class Student:
    def __init__(self, student_id, name, dob):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__marks = {}
        self.__gpa = 0.0

    def set_mark(self, course_id, mark):
        rounded_mark = math.floor(mark * 10) / 10 
        self.__marks[course_id] = rounded_mark

    def get_mark(self, course_id):
        return self.__marks.get(course_id, None)

    def calculate_gpa(self, courses):
        total_weighted_marks = 0
        total_credits = 0
        for course_id, mark in self.__marks.items():
            course = next((c for c in courses if c.get_id() == course_id), None)
            if course:
                total_weighted_marks += mark * course.get_credits()
                total_credits += course.get_credits()
        if total_credits > 0:
            self.__gpa = total_weighted_marks / total_credits
        else:
            self.__gpa = 0.0

    def get_gpa(self):
        return self.__gpa

    def __str__(self):
        return f"ID: {self.__student_id}, Name: {self.__name}, DoB: {self.__dob}, GPA: {self.__gpa:.2f}"

    def list_marks(self):
        return self.__marks
