"""Створюємо класи Student та Group"""
class Student:
    """Клас,який містить інформацію про учнів, рахує середню оцінку учня"""
    def __init__(self, student_id, name, grades=[]):
        """Метод, що ініціалізує атрибути класу"""
        self.student_id = student_id
        self.name = name
        self.grades = grades

    def calculate_average_grade(self):
        """Метод,що рахує середню оцінку учня"""
        average_grade = 0
        if len(self.grades) > 0:
            average_grade = round(sum(self.grades) / len(self.grades), 2)
        return average_grade

    def __str__(self):
        return f"Student {self.name}, ID: {self.student_id}, Average Grade: {self.calculate_average_grade()}"
    
class Group:
    """Клас, який містить ліст, в якому є учні, рахує середній бал групи"""
    def __init__(self, students = []):
        """Метод, що ініціалізує атрибут класу"""
        self.students = students

    def add_student(self, student):
        """Метод, що додає учнів в ліст"""
        self.students.append(student)

    def remove_student(self, student):
        """Метод, що видаляє учня з ліста"""
        if student in self.students:
            self.students.remove(student)
        else:
            print(f"{student.name} not found in the group.")
    
    def list_students(self):
        """Метод, що виводить всіх учнів"""
        for student in self.students:
            print(student)

    def calculate_group_average_grade(self):
        """Метод, що  рахує середню оцінку групи"""
        total_grades = 0
        total_students = 0
        for student in self.students:
            total_grades += sum(student.grades)
            total_students += len(student.grades)
        if total_students == 0:
            return 0
        return round(total_grades / total_students, 2)
    
if __name__ == "__main__":
    student1 = Student(1, "Даніель", [90, 85, 95])
    student2 = Student(2, "Максим", [92, 88, 76])
    student3 = Student(3, "Іван", [85, 89, 45])

    group = Group()
    group.add_student(student1)
    group.add_student(student2)
    group.add_student(student3)

    group.list_students()

    print("Group Average Grade:", group.calculate_group_average_grade())
    