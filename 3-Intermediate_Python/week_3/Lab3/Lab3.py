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
        # at first i was confused when seeing x:y, I assumed it was referencing the key vlaue pairs
        # but it starts with x and y (the first two elements, in this case, the values of the self.courses dictionary), then keeps adding til all the elements are summed
        # then it assigns that total in total_grades
        total_grades = reduce(lambda x, y: x+y, self.courses.values())

        return total_grades / total_courses
    
    def addCourse(self, course, score):
        assert isinstance(course, str), "Course must be a word or series of words."
        assert isinstance(score, float), "Score must be a number."
        assert 0<=score<=4, "Score must be between 0 and 4."

        new_course = {course: score}
        self.courses.update(new_course)
    
    def addCourses(self, courses):
        assert isinstance(courses, dict), "Courses must be in 'key':\"value\" pairs."

        self.courses.update(courses)

    def __str__(self):
        gpa_str = f"{self.gpa():3f}"
        courses_str = ",".join(self.courses.keys())

        return f"{self.id:<6} {self.lastName:<10} {self.firstName:<10} {gpa_str:<5} {courses_str:<10}"

    def __rpr__(self):
        return f"{self.id}, {self.lastName}, {self.firstName}, {self.courses}"

    def header():
        return f"{'ID':<6} {'Last Name':<10} {'First Name':<10} {'GPA':<5} {'Courses':>10}\n {'='*80}"
    
    def printStudents(students):
        print(Student.header())
        for student in students:
            print(student)
    

if __name__ == "__main__":
    students = []
    students.append(Student(123456, "Johnnie", "Smith", {'CSE-101': 3.50, 'CSE-102': 3.00, 'CSE-201': 4.00, 'CSE-220': 3.75, 'CSE-325': 4.00}))
    students.append(Student(234567, "Jamie", "Strauss", {'CSE-101': 3.00, 'CSE-103': 3.50, 'CSE-202': 3.25, 'CSE-220': 4.00, 'CSE-401': 4.00}))
    students.append(Student(345678, "Jack", "O'Neill", {'CSE-101': 2.50, 'CSE-102': 3.50, 'CSE-103': 3.00, 'CSE-104': 4.00}))
    students.append(Student(456789, "Susie", "Marks", {'CSE-101': 4.00, 'CSE-103': 2.50, 'CSE-301': 3.50, 'CSE-302': 3.00, 'CSE-310': 4.00}))
    students.append(Student(567890, "Frank", "Marks", {'CSE-102': 4.00, 'CSE-104': 3.50, 'CSE-201': 2.50, 'CSE-202': 3.50, 'CSE-203': 3.00}))
    students.append(Student(654321, "Annie", "Marks", {'CSE-101': 4.00, 'CSE-102': 4.00, 'CSE-103': 3.50, 'CSE-201': 4.00, 'CSE-203': 4.00}))
    students.append(Student(987456, "Judy", "Smith", {'CSE-102': 4.00, 'CSE-103': 4.00, 'CSE-201': 3.00, 'CSE-210': 3.50, 'CSE-310': 4.00}))
    students.append(Student(456987, "John", "Smith"))
    students[-1].addCourse('CSE-102', 4.00)
    students[-1].addCourse('CSE-103', 4.00)
    students[-1].addCourse('CSE-201', 3.00)
    students[-1].addCourse('CSE-210', 3.50)
    students[-1].addCourse('CSE-310', 4.00)
    students.append(Student(111354, "Kelly", "Williams"))
    students[-1].addCourse('CSE-101', 3.50)
    students[-1].addCourse('CSE-102', 3.50)
    students[-1].addCourse('CSE-201', 3.00)
    students[-1].addCourse('CSE-202', 3.50)
    students[-1].addCourse('CSE-203', 3.50)
    students.append(Student(995511, "Brad", "Williams"))
    students[-1].addCourse('CSE-102', 3.00)
    students[-1].addCourse('CSE-110', 3.50)
    students[-1].addCourse('CSE-125', 3.50)
    students[-1].addCourse('CSE-201', 4.00)
    students[-1].addCourse('CSE-203', 3.00)

    print("\nQuery 1 - Sorted by last then first name:\n")
    sorted_students = sorted(students, key=lambda student: (student.lastName, student.firstName))
    Student.printStudents(sorted_students)

    print("\nQuery 2 - Sorted by last then GPA:\n")
    sorted_gpa = sorted(students, key=lambda student: student.gpa())
    Student.printStudents(sorted_gpa)

    print("\nQuery 3 - Unique Courses:\n")
    # this also look a while to figure out
    # for course in student.courses iterates over each key in the courses dictionary of the student objects
    # student.course is referring to the Student class with parameter courses
    # for student in students iterates over each student object in teh students list
    unique_courses = {course for student in students for course in student.courses}
    print(unique_courses)

    print("\nQuery 4 - Get a list of students who have taken 'CSE-201:\n")
    unique_student = {student for student in students if 'CSE-201' in student.courses}
    for student in unique_student:
        print(student)

    print("\nQuery 5 - Get a list of students who have taken 'CSE-201:\n")
    honor_roll = [student for student in students if student.gpa()>=3.5]
    Student.printStudents(honor_roll)