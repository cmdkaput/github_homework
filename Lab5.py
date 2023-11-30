"""Creating Student and Group classes"""
class Student:
    """The class, which contains information about students, calculates the student's average grade"""
    def __init__(self, student_id, name, grades=[]):
        """Method that initializes class attributes"""
        self.student_id = student_id
        self.name = name
        self.grades = grades

    def calculate_average_grade(self):
        """Method that calculates student's average grade"""
        average_grade = 0
        if len(self.grades) > 0:
            average_grade = round(sum(self.grades) / len(self.grades), 2)
        return average_grade

    def __str__(self):
        return f"Student {self.name}, ID: {self.student_id}, Average Grade: {self.calculate_average_grade()}"
    
class Group:
    """Class which contains a list, that has students in and calculates the average grade of the group"""
    def __init__(self, students = []):
        """Method that initializes class attributes"""
        self.students = students

    def add_student(self, student):
        """Method of adding student to list"""
        self.students.append(student)

    def remove_student(self, student):
        """Method of removing student to list"""
        if student in self.students:
            self.students.remove(student)
        else:
            print(f"{student.name} not found in the group.")
    
    def list_students(self):
        """Method that prints all the students"""
        for student in self.students:
            print(student)

    def calculate_group_average_grade(self):
        """Method that calculates the average grade of the group"""
        total_grades = 0
        total_students = 0
        for student in self.students:
            total_grades += sum(student.grades)
            total_students += len(student.grades)
        if total_students == 0:
            return 0
        return round(total_grades / total_students, 2)
    
if __name__ == "__main__":
    student1 = Student(1, "Daniel", [90, 85, 95])
    student2 = Student(2, "Max", [92, 88, 76])
    student3 = Student(3, "Ivan", [85, 89, 45])

    group = Group()
    group.add_student(student1)
    group.add_student(student2)
    group.add_student(student3)

    group.list_students()

    print("Group Average Grade:", group.calculate_group_average_grade())
    