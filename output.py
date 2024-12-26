import curses

def init_curses(stdscr):
    curses.curs_set(0)  
    stdscr.clear()
    stdscr.refresh()

def show_student_marks(stdscr, student_manager):
    student_manager.list_courses()
    course_id = input("Enter course ID to show student marks: ")
    stdscr.addstr(0, 0, f"Marks for course {course_id}:")
    row = 1
    for student in student_manager._StudentMarkManager__students:
        mark = student.get_mark(course_id)
        stdscr.addstr(row, 0, f"{student} -> Marks: {mark if mark else 'No marks recorded'}")
        row += 1
    stdscr.refresh()
    stdscr.getch()
