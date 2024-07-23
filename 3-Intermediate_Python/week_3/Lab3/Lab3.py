from functools import reduce

class Student(object):
    def __init__(self, id, firstName, lastName, courses = None):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.courses = dict() if courses is None else courses

    def gpa(self):
        if not self.courses:
            return 0
        total_courses = len(self.courses)
        # EXTRA CREDIT
        # this took a while to figure out but reduce is used when there is an iterable with at least two elements
        # it starts with x and y (the first two elements, in this case, the values of the self.courses dictionary), then keeps adding til all the elements are summed
        # then it assigns that total in total_grades
        total_grades = reduce(lambda x, y: x+y, self.courses.value())

        return total_grades / total_courses
    
    def addCourse(self, course, score):
        assert isinstance(course, str), "Course must be a word or series of words."
        assert isinstance(score, float), "Score must be a number."
        assert 0<score<4, "Score must be between 0 and 4."

        new_course = {course, score}
        self.courses.update(new_course)
    
    def addCourse(self, courses):
        assert isinstance(courses, dict), "Courses must be in 'key':\"value\" pairs."

        self.courses.update(courses)

    def __str__(self):
        gpa_str = f"{self.gpa():3f}"
        courses_str = ",".join(self.courses.keys())

        return f"{self.id:<6} {self.lastName:<10} {self.firstName:<10} {gpa_str:<5} {courses_str:<10}"

    def __rpr__(self):
        return f"{self.id}, {self.lastName}, {self.firstName}, {self.courses}"

    def header():
        return f"{"ID":<6} {"Last Name":<10} {"First Name:<10"} {"GPA":<5} {"Courses":<10}\n {"="*40}"