from src.person import Person

# Create Student class that inherits the Person class 
class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        """Add or update the grade for a specified subject."""
        self.grades[subject] = grade

    def enroll_course(self, course):
        """Enroll the student in a specified course."""
        self.courses.append(course)

    def display_student_info(self):
        """Print all details of the student, including enrolled courses and grades."""
        print(f"Student Information:\n"
              f"Name: {self.name}\n"
              f"ID: {self.student_id}\n"
              f"Age: {self.age}\n"
              f"Address: {self.address}\n"
              f"Enrolled Courses: {', '.join(self.courses) if self.courses else 'None'}\n"
              f"Grades: {self.grades if self.grades else 'None'}")
