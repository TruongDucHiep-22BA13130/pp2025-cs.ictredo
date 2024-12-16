class Student:  
    def __init__(self, student_id, name, dob):  
        self.student_id = student_id  
        self.name = name  
        self.dob = dob  
        self.marks = {}  

    def set_marks(self, course_id, mark):  
        self.marks[course_id] = mark  

    def get_marks(self, course_id):  
        return self.marks.get(course_id, None)  

    def __str__(self):  
        return f"{self.student_id} - {self.name} - {self.dob}"  

class Course:  
    def __init__(self, course_id, name):  
        self.course_id = course_id  
        self.name = name  

    def __str__(self):  
        return f"{self.course_id} - {self.name}"  

class StudentMarkManagement:  
    def __init__(self):  
        self.students = []  
        self.courses = []  

    def input_number_of_students(self):  
        num_students = int(input("Enter the number of students: "))  
        for _ in range(num_students):  
            student_id = input("Enter student ID: ")  
            name = input("Enter student name: ")  
            dob = input("Enter student Date of Birth (YYYY-MM-DD): ")  
            student = Student(student_id, name, dob)  
            self.students.append(student)  

    def input_number_of_courses(self):  
        num_courses = int(input("Enter the number of courses: "))  
        for _ in range(num_courses):  
            course_id = input("Enter course ID: ")  
            name = input("Enter course name: ")  
            course = Course(course_id, name)  
            self.courses.append(course)  

    def select_course_and_input_marks(self):  
        self.list_courses()  
        course_id = input("Select a course ID to input marks: ")  
        for student in self.students:  
            mark = float(input(f"Enter marks for {student.name} (ID: {student.student_id}) in course {course_id}: "))  
            student.set_marks(course_id, mark)  


    def list_courses(self):  
        print("Courses List:")  
        for course in self.courses:  
            print(course)  

    def list_students(self):  
        print("Students List:")  
        for student in self.students:  
            print(student)  

    def show_student_marks(self):  
        self.list_courses()  
        course_id = input("Enter course ID to show student marks: ")  
        print(f"Marks for course {course_id}:")  
        for student in self.students:  
            mark = student.get_marks(course_id)  
            if mark is not None:  
                print(f"{student.name} (ID: {student.student_id}): {mark}")  
            else:  
                print(f"{student.name} (ID: {student.student_id}): No marks recorded")  

