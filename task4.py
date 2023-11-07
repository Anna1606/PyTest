# Тест на создание объектов студента и учителя:
#
# Создайте несколько объектов студентов и учителя с разными кодами и именами.
# Убедитесь, что созданные объекты корректно хранят информацию о коде, имени и типе (студент или учитель).
# Тест на вывод информации:
#
# Создайте объекты студентов и учителя.
# Запустите код для вывода информации о них.
# Проверьте, что вывод информации соответствует ожидаемому формату.
# Тест на обработку разных типов объектов:
#
# Попробуйте создать объекты студентов и учителя с неправильными типами данных (например, передать строку вместо кода).
# Проверьте, что код корректно обрабатывает такие ситуации и генерирует ошибки или исключения при необходимости.
# Тест на уникальность кодов:
#
# Попробуйте создать объекты студентов и учителя с одинаковыми кодами.
# Убедитесь, что код обрабатывает такие ситуации и не позволяет создать объекты с одинаковыми кодами.
# Тест на изменение информации:
#
# Создайте объект студента.
# Измените его имя или тип.
# Убедитесь, что информация об объекте корректно обновляется.

from task3 import Person, Student, Teacher

import unittest


class TestTask4(unittest.TestCase):

    # Выполняется перед каждым тестом
    def setUp(self):
        # Создание списка студентов и учителя
        self.student = Student("ОВ", "Олег Воропаев")
        self.teacher = Teacher("БЛ", "Бадеев Леонид")

    def test_student_data(self):
        code = self.student.code
        self.assertEqual(code, "ОВ", "Код не верный")  # второе условие выводится в случае провала теста
        name = self.student.name
        self.assertEqual(name, "Олег Воропаев", "Имя не верное")
        type = self.student.type
        self.assertEqual(type, "Студент", "Тип не верный")

    def test_teacher_data(self):
        code = self.teacher.code
        self.assertEqual(code, "БЛ", "Код не верный")
        name = self.teacher.name
        self.assertEqual(name, "Бадеев Леонид", "Имя не верное")
        type_teacher = self.teacher.type
        self.assertEqual(type_teacher, "Преподаватель", "Тип не верный")

# Тест на вывод информации:
# Создайте объекты студентов и учителя.
# Запустите код для вывода информации о них.
# Проверьте, что вывод информации соответствует ожидаемому формату.


def test_output(capsys):
    student = Student("ОВ", "Олег Воропаев")
    teacher = Teacher("БЛ", "Бадеев Леонид")

    # Вывод информации о студентах и учителе
    print(f"Код: {student.code}, Имя: {student.name}, Тип: {student.type}")
    captured = capsys.readouterr()
    assert captured.out == "Код: ОВ, Имя: Олег Воропаев, Тип: Студент\n"

    print(f"Код: {teacher.code}, Имя: {teacher.name}, Тип: {teacher.type}")
    captured = capsys.readouterr()
    assert captured.out == "Код: БЛ, Имя: Бадеев Леонид, Тип: Преподаватель\n"