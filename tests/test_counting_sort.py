from unittest.mock import patch

from src.sort.counting_sort import count, counting_sort


class TestCountingSortMode:
    """Тесты для режима сортировки подсчетом"""
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    @patch('src.validation.sort_int_validation')
    def test_valid_input_sorts_numbers(self, mock_validation, mock_secho, mock_print, mock_input):
        """Тест: валидный ввод - сортирует числа"""
        mock_input.side_effect = ['3 1 2', 'back']
        mock_validation.return_value = (True, "")
        
        counting_sort()
        
        mock_print.assert_called_once_with(1, 2, 3)
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    @patch('src.validation.sort_int_validation')
    def test_invalid_input_shows_error(self, mock_validation, mock_secho, mock_print, mock_input):
        """Тест: невалидный ввод - показывается ошибка"""
        mock_input.side_effect = ['3 abc 2', 'back']
        mock_validation.return_value = (False, "Элемент 'abc' не является целым числом")
        
        counting_sort()
        
        mock_secho.assert_called_once_with("Элемент 'abc' не является целым числом", fg='red')
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_exit_commands_work(self, mock_secho, mock_print, mock_input):
        """Тест: команды выхода работают"""
        for exit_cmd in ['back', 'b', 'q']:
            mock_input.side_effect = [exit_cmd]
            
            counting_sort()
            
            mock_print.assert_not_called()
            mock_secho.assert_not_called()


class TestCountFunction:
    """Тесты для функции count"""
    
    def test_count_sort_positive_numbers(self):
        """Тест функции сортировки подсчетом для положительных чисел и пустого списка"""
        assert count([3, 1, 2]) == [1, 2, 3]
        assert count([5, 2, 8, 1]) == [1, 2, 5, 8]
        assert count([1, 2, 3]) == [1, 2, 3]
        assert count([10, 1, 100]) == [1, 10, 100]
        assert count([1]) == [1]
        assert count([]) == []
    
    def test_count_sort_negative_numbers(self):
        """Тест функции сортировки подсчетом для отрицательных чисел"""
        assert count([-1, -3, -2]) == [-3, -2, -1]
        assert count([0, -5, 5]) == [-5, 0, 5]
        assert count([-3, -2, -1]) == [-3, -2, -1]
    
    def test_count_sort_duplicate_numbers(self):
        """Тест функции сортировки подсчетом с дубликатами"""
        assert count([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]
        assert count([2, 2, 2, 1]) == [1, 2, 2, 2]