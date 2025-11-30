from unittest.mock import patch

from src.sort.quick_sort import quick, quick_sort


class TestQuickSortMode:
    """Тесты для режима быстрой сортировки"""

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    @patch('src.validation.sort_int_validation')
    def test_valid_input_sorts_numbers(self, mock_validation, mock_secho, mock_print, mock_input):
        """Тест: валидный ввод - сортирует числа"""
        mock_input.side_effect = ['3 1 2', 'back']
        mock_validation.return_value = (True, "")

        quick_sort()

        mock_print.assert_called_once_with(1, 2, 3)

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    @patch('src.validation.sort_int_validation')
    def test_invalid_input_shows_error(self, mock_validation, mock_secho, mock_print, mock_input):
        """Тест: невалидный ввод - показывается ошибка"""
        mock_input.side_effect = ['3 abc 2', 'back']
        mock_validation.return_value = (False, "Элемент 'abc' не является целым числом")

        quick_sort()

        mock_secho.assert_called_once_with("Элемент 'abc' не является целым числом", fg='red')

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_exit_commands_work(self, mock_secho, mock_print, mock_input):
        """Тест: команды выхода работают"""
        for exit_cmd in ['back', 'b', 'q']:
            mock_input.side_effect = [exit_cmd]

            quick_sort()

            mock_print.assert_not_called()
            mock_secho.assert_not_called()


class TestQuickFunction:
    """Тесты для функции quick"""

    def test_quick_sort_positive_numbers(self):
        """Тест функции быстрой сортировки для чисел и пустых строк"""
        assert quick([3, 1, 2]) == [1, 2, 3]
        assert quick([5, 2, 8, 1]) == [1, 2, 5, 8]
        assert quick([-1, -3, -2]) == [-3, -2, -1]
        assert quick([0, -5, 5]) == [-5, 0, 5]
        assert quick([1, 2, 3]) == [1, 2, 3]
        assert quick([-3, -2, -1]) == [-3, -2, -1]
        assert quick([1]) == [1]
        assert quick([]) == []

    def test_quick_sort_duplicate_numbers(self):
        """Тест функции быстрой сортировки с дубликатами"""
        assert quick([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]
        assert quick([2, 2, 2, 1]) == [1, 2, 2, 2]
