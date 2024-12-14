class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Учня {student} додано до класу.")

    def list_students(self):
        if self.students:
            print("Учні в класі:")
            for student in self.students:
                print(f" - {student}")
        else:
            print("Клас поки порожній.")

classroom = Classroom()

student1 = Student("Джонни")
student2 = Student("Петро")

classroom.add_student(student1)
classroom.add_student(student2)

classroom.list_students()