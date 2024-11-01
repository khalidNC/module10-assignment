from src.person import Person
from src.student import Student
from src.course import Course

# Test person
person1 = Person("Alice", 30, "123 Elm Street")
person1.display_person_info()

# Test student
student1 = Student("khalid", 42, "187 dohs", '00008')
student1.add_grade("Math", "A")
student1.enroll_course("Science")
student1.display_student_info()

# Test course
student2 = Student("Hussain", 20, "123 Elm Street", "S001")
course1 = Course("Math Applied", "AM01", "K Hussian")
course1.add_student(student2)
course1.display_course_info()
