import curses
from domains.student import Student
from domains.course import Course
from domains.student_mark_manager import StudentMarkManager
import input
import output

def main(stdscr):
    student_manager = StudentMarkManager()
    output.init_curses(stdscr)

    num_students = input.input_number_of_students()
    for _ in range(num_students):
        student_id, name, dob = input.input_student_data()
        student = Student(student_id, name, dob)
        student_manager.add_student(student)

    num_courses = input.input_number_of_courses()
    for _ in range(num_courses):
        course_id, name, credits = input.input_course_data()
        course = Course(course_id, name, credits)
        student_manager.add_course(course)

    student_manager.input_marks_for_courses()
    student_manager.calculate_gpa_for_all_students()
    student_manager.sort_students_by_gpa()
    output.show_student_marks(stdscr, student_manager)

if __name__ == "__main__":
    curses.wrapper(main)
