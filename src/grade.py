# Created grade class 
class Grade:
    def __init__(self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade
    
    # This special method will display actual text when it is print
    def __str__(self):
        return f"Grade: {self.grade} - {self.student.name} in {self.course.course_name}"
