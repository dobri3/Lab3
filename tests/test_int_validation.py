from src.validation.sort_int_validation import sort_int_validation


class TestSortIntValidation:
    """Тесты для валидации списка целых чисел"""

    def test_valid_integers(self):
        """Тест: валидные целые числа - True"""
        result, message = sort_int_validation(["1", "5", "10", "-3"])
        assert result is True
        assert message == ""

    def test_empty_list(self):
        """Тест: пустой список - True"""
        result, message = sort_int_validation([])
        assert result is True
        assert message == ""

    def test_not_number_in_list(self):
        """Тест: не число в списке - False с ошибкой"""
        result, message = sort_int_validation(["1", "abc", "5"])
        assert result is False
        assert "не является целым числом" in message
        assert "abc" in message

    def test_float_in_list(self):
        """Тест: дробное число в списке - False с ошибкой"""
        result, message = sort_int_validation(["1", "3.14", "5"])
        assert result is False
        assert "не является целым числом" in message
