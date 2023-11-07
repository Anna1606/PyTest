import unittest


class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль недопустимо")
        return a / b


# в скобках указывается наследование класса
class TestCalculator(unittest.TestCase):

    # Выполняется перед каждым тестом
    def setUp(self):
        self.calculator = Calculator()

    # Выполняется после каждого теста
    def tearDown(self):
        # Дополнительный код очистки, если необходимо
        pass

    def test_add(self):
        result = self.calculator.add(5, 3)
        self.assertEqual(result, 8, "Сложение работает неверно")

    def test_subtract(self):
        result = self.calculator.subtract(10, 4)
        self.assertEqual(result, 6, "Вычитание работает неверно")

    def test_multiply(self):
        result = self.calculator.multiply(2, 3)
        self.assertEqual(result, 6, "Умножение работает неверно")

    def test_divide(self):
        result = self.calculator.divide(8, 4)
        self.assertEqual(result, 2, "Деление работает неверно")

    # тестирование на выброс исключений
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)

    @unittest.skip("Пропустить этот тест")
    def test_skip_example(self):
        self.fail("Этот тест не должен быть выполнен")

    @unittest.skipIf(True, "Пропустить этот тест при определенном условии")
    def test_skip_if_example(self):
        self.fail("Этот тест не должен быть выполнен из-за условия")

    @unittest.expectedFailure
    def test_expected_failure(self):
        result = self.calculator.add(2, 2)
        self.assertEqual(result, 5, "Ожидаемый провал")