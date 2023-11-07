"""
Модуль для сравнения средних значений двух списков целых чисел
"""


class CompareAverageValueTwoLists:
    """
    Сравнение средних значений двух списков целых чисел
    """

    def __init__(self, list_1, list_2):
        """
        Конструктор сравнения средних чисел двух списков
        :param list_1: первый список целых чисел
        :param list_2: второй список целых чисел
        """
        if len(list_1) > 0 and len(list_2) > 0:
            self.list_1 = list_1
            self.list_2 = list_2
            self.sum_list_value_1 = self.find_sum_list_values(list_1)
            self.sum_list_value_2 = self.find_sum_list_values(list_2)
        else:
            raise ValueError("Вы передали пустой список")

    def find_sum_list_values(self, list_values):
        """
        Метод нахождения суммы списка чисел
        :param list_values: список чисел
        :return: сумма списка чисел
        """
        sum_all_numbers = 0
        for i in list_values:
            sum_all_numbers += i
        return sum_all_numbers

    def find_list_average_value(self, sum_list_values, len_list):
        """
        Метод нахождения среднего значения списка чисел
        :param sum_list_values: сумма списка чисел
        :param len_list: длина списка чисел
        :return: среднее значение списка чисел
        """
        return sum_list_values / len_list

    def compare_average_lists_values(self):
        """
        Метод сравнения средних значений двух списков
        :return: результат сравнения
        """
        average_value_1 = self.find_list_average_value(self.sum_list_value_1, len(self.list_1))
        average_value_2 = self.find_list_average_value(self.sum_list_value_2, len(self.list_2))
        result = ""
        if average_value_1 == average_value_2:
            result = "Средние значения равны"
        if average_value_1 > average_value_2:
            result = "Первый список имеет большее среднее значение"
        if average_value_1 < average_value_2:
            result = "Второй список имеет большее среднее значение"
        return result

# if __name__ == "__main__":
#     comparator = CompareAverageValueTwoLists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
#     print(comparator.compare_average_lists_values())
