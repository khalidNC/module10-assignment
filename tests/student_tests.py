# tests/test_student.py

from src.person import Person
from src.student import Student
from src.course import Course

# Create instances
student1 = Student("Hussain", 20, "123 Elm Street", "S001")
course1 = Course("Math Applied", "AM01", "K Hussain")

# Enroll the student and assign a grade
course1.add_student(student1)
course1.assign_grade(student1, "A")

# Display grades for the student
student1.display_grades()
