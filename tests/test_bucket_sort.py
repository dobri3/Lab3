from unittest.mock import patch

from src.sort.bucket_sort import bucket, bucket_sort


class TestBucketSortMode:
    """Тесты для режима карманной сортировки"""

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    @patch('src.validation.sort_float_validation')
    def test_valid_input_sorts_numbers(self, mock_validation, mock_secho, mock_print, mock_input):
        """Тест: валидный ввод -> сортирует числа"""
        mock_input.side_effect = ['0.3 0.1 0.2', '3', 'back']
        mock_validation.return_value = (True, "")

        bucket_sort()

        mock_print.assert_called_once()

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    @patch('src.validation.sort_float_validation')
    def test_invalid_buckets_shows_error(self, mock_validation, mock_secho, mock_print, mock_input):
        """Тест: невалидное количество карманов -> показывается ошибка"""
        mock_input.side_effect = ['0.3 0.1 0.2', '0', 'back']
        mock_validation.return_value = (True, "")

        bucket_sort()

        mock_secho.assert_called_once_with("Buckets must be greater than 0", fg='red')

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    @patch('src.validation.sort_float_validation')
    def test_invalid_input_shows_error(self, mock_validation, mock_secho, mock_print, mock_input):
        """Тест: невалидный ввод -> показывается ошибка"""
        mock_input.side_effect = ['0.5 1.5 0.2', '3', 'back']
        mock_validation.return_value = (False, "Не выполнено условия '0<=x<1' для [1.5]")

        bucket_sort()

        mock_secho.assert_called_once_with("Не выполнено условия '0<=x<1' для [1.5]", fg='red')

    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_exit_commands_work(self, mock_secho, mock_print, mock_input):
        """Тест: команды выхода работают"""
        for exit_cmd in ['back', 'b', 'q']:
            mock_input.side_effect = [exit_cmd]

            bucket_sort()

            mock_print.assert_not_called()
            mock_secho.assert_not_called()


class TestBucketFunction:
    """Тесты для функции bucket"""

    def test_bucket_sort_valid_numbers(self):
        """Тест функции карманной сортировки для валидных чисел"""
        assert bucket([0.3, 0.1, 0.2], 3) == [0.1, 0.2, 0.3]
        assert bucket([0.5], 2) == [0.5]
        assert bucket([], 3) == []
        assert bucket([0.3, 0.1, 0.3, 0.2, 0.1], 3) == [0.1, 0.1, 0.2, 0.3, 0.3]


    def test_bucket_sort_multiple_buckets(self):
        """Тест функции карманной сортировки с разным количеством карманов"""
        input_list = [0.1, 0.5, 0.9, 0.2, 0.8]

        result_2_buckets = bucket(input_list, 2)
        result_5_buckets = bucket(input_list, 5)

        assert result_2_buckets == [0.1, 0.2, 0.5, 0.8, 0.9]
        assert result_5_buckets == [0.1, 0.2, 0.5, 0.8, 0.9]
