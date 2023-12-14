class Course:
    def __init__(self, course_code, title, max_capacity):
        self.course_code = course_code
        self.title = title
        self.max_capacity = max_capacity
        self.current_students = 0

    def enroll(self, student):
        if self.current_students < self.max_capacity:
            self.current_students += 1
            student.courses_enrolled.append(self)
        else:
            print("The course has reached its maximum capacity.")

    def check_slots(self):
        return self.max_capacity - self.current_students

    def display_course_details(self):
        print("Course Code:", self.course_code)
        print("Title:", self.title)
        print("Max Capacity:", self.max_capacity)
        print("Current Number of Students Enrolled:", self.current_students)

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses_enrolled = []

    def display_student_info(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Courses Enrolled:")
        for course in self.courses_enrolled:
            print("   -", course.title)

# File Handling
def write_course_data(course):
    with open('courses.txt', 'a') as f:
        f.write(f"{course.course_code},{course.title},{course.max_capacity}\n")

def write_student_data(student):
    with open('students.txt', 'a') as f:
        f.write(f"{student.student_id},{student.name}\n")

def read_course_data():
    courses = []
    with open('courses.txt', 'r') as f:
        for line in f:
            course_code, title, max_capacity = line.strip().split(',')
            course = Course(course_code, title, int(max_capacity))
            courses.append(course)
    return courses

def read_student_data():
    students = []
    with open('students.txt', 'r') as f:
        for line in f:
            student_id, name = line.strip().split(',')
            student = Student(student_id, name)
            students.append(student)
    return students

def main():
    courses = read_course_data()
    students = read_student_data()

    while True:
        print("\n---MENU---")
        print("1. Display course details")
        print("2. Display student info")
        print("3. Enroll a student in a course")
        print("4. Exit")

        action = input("Select an action (1-4): ")

        if action == "1":
            for course in courses:
                course.display_course_details()
                print("\n")
        elif action == "2":
            for student in students:
                student.display_student_info()
                print("\n")
        elif action == "3":
            course_code = input("Enter the course code you want to enroll in: ")
            student_id = input("Enter the student ID: ")

            course = None
            student = None

            for c in courses:
                if c.course_code == course_code:
                    course = c
                    break

            for s in students:
                if s.student_id == student_id:
                    student = s
                    break

            if course and student:
                course.enroll(student)
                print(f"Student {student.name} has been enrolled in the course {course.title}.")
            else:
                print("The specified course or student could not be found.")
        elif action == "4":
            break
        else:
            print("Invalid selection. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()