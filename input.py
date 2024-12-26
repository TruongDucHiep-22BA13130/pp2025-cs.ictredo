def input_number_of_students():
    num_students = int(input("Enter the number of students: "))
    return num_students

def input_student_data():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
    return student_id, name, dob

def input_number_of_courses():
    num_courses = int(input("Enter the number of courses: "))
    return num_courses

def input_course_data():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    credits = int(input("Enter course credits: "))
    return course_id, name, credits
