import unittest
from unittest import mock  # Import mock from unittest
from io import StringIO  # Import StringIO from the io module
from src.student import Student

class TestStudent(unittest.TestCase):

    def setUp(self):
        """Set up a Student instance for testing."""
        self.student = Student("Alice", 30, "123 Elm Street", "S001")

    def test_initial_attributes(self):
        """Test the initial attributes of the Student."""
        self.assertEqual(self.student.name, "Alice")
        self.assertEqual(self.student.age, 30)
        self.assertEqual(self.student.address, "123 Elm Street")
        self.assertEqual(self.student.student_id, "S001")
        self.assertEqual(self.student.grades, {})
        self.assertEqual(self.student.courses, [])

    def test_add_grade(self):
        """Test adding a grade."""
        self.student.add_grade("Math", "A")
        self.assertEqual(self.student.grades["Math"], "A")

    def test_enroll_course(self):
        """Test enrolling in a course."""
        self.student.enroll_course("Physics")
        self.assertIn("Physics", self.student.courses)

    def test_display_student_info(self):
        """Test displaying student information."""
        self.student.enroll_course("Physics")
        self.student.add_grade("Math", "A")
        expected_output = (
            "Student Information:\n"
            "Name: Alice\n"
            "ID: S001\n"
            "Age: 30\n"
            "Address: 123 Elm Street\n"
            "Enrolled Courses: Physics\n"
            "Grades: {'Math': 'A'}"
        )
        # Capture the output
        with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.student.display_student_info()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == "__main__":
    unittest.main()
