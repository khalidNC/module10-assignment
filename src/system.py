class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")


class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        if subject in self.courses:
            self.grades[subject] = grade
            print(f"Grade {grade} added for {self.name} in {subject}.")
        else:
            print(f"Student not enrolled in {subject}, cannot assign grade.")

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"Student {self.name} (ID: {self.student_id}) enrolled in {course}.")
        else:
            print(f"Student already enrolled in {course}.")

    def display_student_info(self):
        self.display_person_info()
        print(f"ID: {self.student_id}, Courses: {self.courses}, Grades: {self.grades}")


class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Student {student.name} (ID: {student.student_id}) added to {self.course_name}.")
        else:
            print(f"Student {student.name} is already enrolled in {self.course_name}.")

    def display_course_info(self):
        print(f"Course Name: {self.course_name}, Code: {self.course_code}, Instructor: {self.instructor}")
        print("Enrolled Students:", [student.name for student in self.students])
