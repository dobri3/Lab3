from unittest.mock import patch

from src.sort.bubble_sort import bubble, bubble_sort


class TestBubbleSortMode:
    """Тесты для режима сортировки пузырьком"""

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    @patch('src.validation.sort_int_validation')
    def test_valid_input_sorts_numbers(self, mock_validation, mock_secho, mock_print, mock_input):
        """Тест: валидный ввод - сортирует числа"""
        mock_input.side_effect = ['3 1 2', 'back']
        mock_validation.return_value = (True, "")

        bubble_sort()

        mock_print.assert_called_once_with(1, 2, 3)

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    @patch('src.validation.sort_int_validation')
    def test_invalid_input_shows_error(self, mock_validation, mock_secho, mock_print, mock_input):
        """Тест: невалидный ввод - показывается ошибка"""
        mock_input.side_effect = ['3 abc 2', 'back']
        mock_validation.return_value = (False, "Элемент 'abc' не является целым числом")

        bubble_sort()

        mock_secho.assert_called_once_with("Элемент 'abc' не является целым числом", fg='red')

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_exit_commands_work(self, mock_secho, mock_print, mock_input):
        """Тест: команды выхода работают"""
        for exit_cmd in ['back', 'b', 'q']:
            mock_input.side_effect = [exit_cmd]

            bubble_sort()

            mock_print.assert_not_called()
            mock_secho.assert_not_called()


class TestBubbleFunction:
    """Тесты для функции bubble"""

    def test_bubble_sort_positive_numbers(self):
        """Тест функции сортировки пузырьком для положительных чисел и пустого списка"""
        assert bubble([3, 1, 2, 2]) == [1, 2, 2, 3]
        assert bubble([5, 2, 8, 7]) == [2, 5, 7, 8]
        assert bubble([1, 2, 3]) == [1, 2, 3]
        assert bubble([1]) == [1]
        assert bubble([]) == []

    def test_bubble_sort_negative_numbers(self):
        """Тест функции сортировки пузырьком для отрицательных чисел"""
        assert bubble([-1, -3, -2]) == [-3, -2, -1]
        assert bubble([0, -5, 5]) == [-5, 0, 5]
        assert bubble([-3, -2, -1]) == [-3, -2, -1]
