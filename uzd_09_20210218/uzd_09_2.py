# 2021.02.18, Uzd 2:
# Ir dots tuple ar vārdiem (“Alex”, “Carl”, “Hannah”). Izveidot klasi Student, kurai ir atribūts name.
# Izveidot sarakstu ar Student klases objektiem.

class Student:
    def __init__(self, name):
        self.name = name


people = ("Alex", "Carl", "Hannah")

students = [Student(name=name) for name in people]

for student in students:
    print(student.name)
