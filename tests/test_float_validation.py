from src.validation.sort_float_validation import sort_float_validation


class TestSortFloatValidation:
    """Тесты для валидации списка чисел с плавающей точкой"""
    
    def test_valid_floats_in_range(self):
        """Тест: валидные числа в диапазоне 0<=x<1 - True"""
        result, message = sort_float_validation(["0.1", "0.5", "0.99", "0.0"])
        assert result is True
        assert message == ""
    
    def test_number_out_of_range(self):
        """Тест: число вне диапазона - False с ошибкой"""
        result, message = sort_float_validation(["0.5", "1.5", "0.2"])
        assert result is False
        assert "Не выполнено условия" in message
        assert "1.5" in message
    
    def test_negative_number(self):
        """Тест: отрицательное число - False с ошибкой"""
        result, message = sort_float_validation(["0.5", "-0.1", "0.2"])
        assert result is False
        assert "Не выполнено условия" in message
        assert "-0.1" in message
    
    def test_not_number_in_list(self):
        """Тест: не число в списке - False с ошибкой"""
        result, message = sort_float_validation(["0.5", "abc", "0.2"])
        assert result is False
        assert "Не все элементы списка являются числами" in message