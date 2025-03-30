import json
from system import Student, Course


students = {}
courses = {}

def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    address = input("Enter Address: ")
    student_id = input("Enter Student ID: ")
    students[student_id] = Student(name, age, address, student_id)
    print(f"Student {name} (ID: {student_id}) added successfully.")

def add_course():
    course_name = input("Enter Course Name: ")
    course_code = input("Enter Course Code: ")
    instructor = input("Enter Instructor Name: ")
    courses[course_code] = Course(course_name, course_code, instructor)
    print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

def enroll_student_in_course():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    student = students.get(student_id)
    course = courses.get(course_code)
    if student and course:
        student.enroll_course(course.course_name)
        course.add_student(student)
    else:
        print("Invalid student ID or course code.")

def add_grade():
    student_id = input("Enter Student ID: ")
    course_code = input("Enter Course Code: ")
    grade = input("Enter Grade: ")
    student = students.get(student_id)
    if student and course_code in student.courses:
        student.add_grade(course_code, grade)
    else:
        print("Student not enrolled in this course or invalid ID.")

def display_student_details():
    student_id = input("Enter Student ID: ")
    student = students.get(student_id)
    if student:
        student.display_student_info()
    else:
        print("Student not found.")

def display_course_details():
    course_code = input("Enter Course Code: ")
    course = courses.get(course_code)
    if course:
        course.display_course_info()
    else:
        print("Course not found.")

def save_data():
    data = {
        "students": {sid: vars(student) for sid, student in students.items()},
        "courses": {ccode: vars(course) for ccode, course in courses.items()}
    }
    with open("student_management_data.json", "w") as file:
        json.dump(data, file)
    print("All student and course data saved successfully.")

def load_data():
    global students, courses
    try:
        with open("student_management_data.json", "r") as file:
            data = json.load(file)
            # Deserialize students
            students = {
                sid: Student(**details) for sid, details in data["students"].items()
            }
            # Deserialize courses
            courses = {
                ccode: Course(**details) for ccode, details in data["courses"].items()
            }
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("No saved data found.")

def main():
    while True:
        print("\n==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")

        choice = input("Select Option: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            add_course()
        elif choice == '3':
            enroll_student_in_course()
        elif choice == '4':
            add_grade()
        elif choice == '5':
            display_student_details()
        elif choice == '6':
            display_course_details()
        elif choice == '7':
            save_data()
        elif choice == '8':
            load_data()
        elif choice == '0':
            print("Exiting Student Management System. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
