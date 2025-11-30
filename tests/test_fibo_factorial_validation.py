from src.validation.fibo_factorial_validation import fibo_factorial_validation


class TestFiboFactorialValidation:
    """Tесты для функции валидации"""

    def test_positive_number(self):
        """Тест: положительное число - True"""
        result, message = fibo_factorial_validation("5")
        assert result is True
        assert message == ""

    def test_zero(self):
        """Тест: ноль - True"""
        result, message = fibo_factorial_validation("0")
        assert result is True
        assert message == ""

    def test_negative_number(self):
        """Тест: отрицательное число - False с ошибкой"""
        result, message = fibo_factorial_validation("-5")
        assert result is False
        assert "неотрицательным" in message

    def test_not_number(self):
        """Тест: не число - False с ошибкой"""
        result, message = fibo_factorial_validation("abc")
        assert result is False
        assert "не является целым числом" in message

    def test_float_string(self):
        """Тест: дробное число - False с ошибкой"""
        result, message = fibo_factorial_validation("3.14")
        assert result is False
        assert "не является целым числом" in message
