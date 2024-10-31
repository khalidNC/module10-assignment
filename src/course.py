class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name  # Name of the course
        self.course_code = course_code    # Unique course code
        self.instructor = instructor        # Name of the instructor
        self.students = []                  # List to store enrolled students

    def add_student(self, student):
        """Add a student to the course."""
        if student not in self.students:
            self.students.append(student)  # Add the student to the list
        else:
            print(f"Student {student.name} is already enrolled in {self.course_name}.")

    def display_course_info(self):
        """Display the course details."""
        print(f"Course Information:")
        print(f"Course Name: {self.course_name}")
        print(f"Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        print(f"Enrolled Students: {', '.join(student.name for student in self.students)}")