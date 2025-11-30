from unittest.mock import patch

from src.sort.heap_sort import heap, heap_sort, to_heap


class TestHeapSortMode:
    """Тесты для режима сортировки кучей"""

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    @patch('src.validation.sort_int_validation')
    def test_valid_input_sorts_numbers(self, mock_validation, mock_secho, mock_print, mock_input):
        """Тест: валидный ввод - сортирует числа"""
        mock_input.side_effect = ['3 1 2', 'back']
        mock_validation.return_value = (True, "")

        heap_sort()

        mock_print.assert_called_once_with(1, 2, 3)  # отсортированный список

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    @patch('src.validation.sort_int_validation')
    def test_invalid_input_shows_error(self, mock_validation, mock_secho, mock_print, mock_input):
        """Тест: невалидный ввод - показывается ошибка"""
        mock_input.side_effect = ['3 abc 2', 'back']
        mock_validation.return_value = (False, "Элемент 'abc' не является целым числом")

        heap_sort()

        mock_secho.assert_called_once_with("Элемент 'abc' не является целым числом", fg='red')

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_exit_commands_work(self, mock_secho, mock_print, mock_input):
        """Тест: команды выхода работают"""
        for exit_cmd in ['back', 'b', 'q']:
            mock_input.side_effect = [exit_cmd]

            heap_sort()

            mock_print.assert_not_called()
            mock_secho.assert_not_called()


class TestHeapFunction:
    """Тесты для функции heap"""

    def test_heap_sort_numbers(self):
        """Тест функции сортировки кучей для чисел"""
        assert heap([3, 1, 2]) == [1, 2, 3]
        assert heap([5, 2, 8, 1]) == [1, 2, 5, 8]
        assert heap([1]) == [1]
        assert heap([]) == []
        assert heap([-1, -3, -2]) == [-3, -2, -1]
        assert heap([0, -5, 5]) == [-5, 0, 5]
        assert heap([1, 2, 3]) == [1, 2, 3]
        assert heap([-3, -2, -1]) == [-3, -2, -1]

    def test_heap_sort_duplicate_numbers(self):
        """Тест функции сортировки кучей с дубликатами"""
        assert heap([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]
        assert heap([2, 2, 2, 1]) == [1, 2, 2, 2]


class TestToHeapFunction:
    """Тесты для вспомогательной функции to_heap"""

    def test_to_heap_builds_max_heap(self):
        """Тест функции to_heap для построения max-heap"""
        arr = [3, 1, 2, 5]
        to_heap(arr, len(arr), 0)
        assert arr[0] == 3

    def test_to_heap_with_single_element(self):
        """Тест функции to_heap с одним элементом"""
        arr = [5]
        to_heap(arr, len(arr), 0)
        assert arr == [5]

    def test_to_heap_with_two_elements(self):
        """Тест функции to_heap с двумя элементами"""
        arr = [1, 3]
        to_heap(arr, len(arr), 0)
        assert arr[0] == 3
