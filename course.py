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
