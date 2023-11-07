class Person:
    def __init__(self, code, name):
        self.code = code
        self.name = name


class Student(Person):
    def __init__(self, code, name):
        super().__init__(code, name)
        self.type = "Студент"


class Teacher(Person):
    def __init__(self, code, name):
        super().__init__(code, name)
        self.type = "Преподаватель"

# # Создание списка студентов и учителя
# students = [
#     Student("ОВ", "Олег Воропаев"),
#     Student("СК", "Сергей Казицын"),
#     Student("МБ", "Максим Бобков"),
#     Student("ЕН", "Елена Некрашевич"),
#     Student("ДА", "Дмитрий Артемьев"),
#     Student("ИП", "Инна Пешкова"),
#     Student("ТН", "Тимур Николаев"),
#     Student("ТР", "Терёшин Роман"),
#     Student("АП", "Александр Политов"),
# ]
#
# teacher = Teacher("БЛ", "Бадеев Леонид")
#
# # Вывод информации о студентах и учителе
# for student in students:
#     print(f"Код: {student.code}, Имя: {student.name}, Тип: {student.type}")
#
# print(f"Код: {teacher.code}, Имя: {teacher.name}, Тип: {teacher.type}")
