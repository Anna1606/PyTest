"""
Модуль для тестирования модуля comporator.py
"""
import unittest

from HW.comparator import CompareAverageValueTwoLists


class TestComparator(unittest.TestCase):
    """
    Класс для тестирования модуля comporator.py
    """

    def setUp(self):
        """
        Конструктор компоратора для тестирования
        :return: объект компоратора
        """
        self.list_1 = [1, 3, 5, 7, 9]
        self.list_2 = [2, 4, 6, 8, 10]
        self.comporator = CompareAverageValueTwoLists(self.list_1, self.list_2)

    def test_null_list(self):
        """
        Проверяем исключение при передаче пустых списков
        """
        list_1 = []
        list_2 = []
        with self.assertRaises(ValueError) as context:
            CompareAverageValueTwoLists(list_1, list_2)
        self.assertEqual(str(context.exception),
                         "Вы передали пустой список")

    def test_correct_add_lists(self):
        """
        Тестируем корректную запись списков в компоратор
        """
        list_1 = [1, 3, 5, 7, 9]
        list_2 = [2, 4, 6, 8, 10]
        self.assertEqual(self.comporator.list_1, list_1, "Ошибка записи первого списка")
        self.assertEqual(self.comporator.list_2, list_2, "Ошибка записи второго списка")

    def test_find_sum_list_values(self):
        """
        Тестируем корректность расчета суммы списка чисел
        """
        sum_list_1 = self.comporator.find_sum_list_values(self.list_1)
        sum_list_2 = self.comporator.find_sum_list_values(self.list_2)
        self.assertEqual(sum_list_1, 25, "Сумма списка неверна")
        self.assertEqual(sum_list_2, 30, "Сумма списка неверна")

    def test_find_list_average_value(self):
        """
        Тестирование метода расчета среднего значения списка
        """
        sum_list_values_1 = self.comporator.sum_list_value_1
        len_list_1 = len(self.list_1)
        assert 5 == self.comporator.find_list_average_value(sum_list_values_1, len_list_1)

        sum_list_values_2 = self.comporator.sum_list_value_2
        len_list_2 = len(self.list_2)
        assert 6 == self.comporator.find_list_average_value(sum_list_values_2, len_list_2)

    def test_compare_average_lists_values(self):
        """
        Тестирование метода сравнения двух чисел
        """
        result = self.comporator.compare_average_lists_values()
        assert result == "Второй список имеет большее среднее значение"

        list_1 = [1, 3, 5, 7, 9]
        list_2 = [2, 4, 6, 3]
        comporator_1 = CompareAverageValueTwoLists(list_1, list_2)
        result_1 = comporator_1.compare_average_lists_values()
        assert result_1 == "Первый список имеет большее среднее значение"

        list_3 = [1, 3, 4, 3]
        list_4 = [1, 3, 4, 3]
        comporator_2 = CompareAverageValueTwoLists(list_3, list_4)
        result_2 = comporator_2.compare_average_lists_values()
        assert result_2 == "Средние значения равны"
