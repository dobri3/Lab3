from unittest.mock import patch

from src.fibo import fibo, fibo_recursive, fibonachi
    

class TestFibonachiMode:
    """Тесты для режима числа Фибоначчи"""
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_valid_input_calculates_fibonachi(self, mock_secho, mock_print, mock_input):
        """Тест: валидный ввод - вычисляется число Фибоначчи"""
        mock_input.side_effect = ['5', 'back']
        
        fibonachi()
        
        mock_print.assert_called_once_with(5)
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_invalid_input_shows_error(self, mock_secho, mock_print, mock_input):
        """Тест: невалидный ввод - показывается ошибка"""
        mock_input.side_effect = ['-5', 'back']
        
        fibonachi()
        
        mock_secho.assert_called_once()
        assert mock_secho.call_args[1]['fg'] == 'red'
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_exit_commands_work(self, mock_secho, mock_print, mock_input):
        """Тест: команды выхода работают"""
        for exit_cmd in ['back', 'b', 'q']:
            mock_input.side_effect = [exit_cmd]
            
            fibonachi()
            
            mock_print.assert_not_called()
            mock_secho.assert_not_called()

class TestFibo:
    def test_fac_positive_numbers(self):
        """Тест итеративной функции числа Фибоначчи для положительных чисел"""
        assert fibo(0) == 0
        assert fibo(1) == 1
        assert fibo(2) == 1
        assert fibo(3) == 2
        assert fibo(5) == 5
        assert fibo(7) == 13

class TestFibonachiRecurciveMode:
    """Тесты работа мода реурсивного числа Фибоначчи"""
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_valid_input_calculates_factorial_rec(self, mock_secho, mock_print, mock_input):
        """Тест: валидный ввод - вычисляется число Фибоначчи"""
        mock_input.side_effect = ['5', 'back']
        
        fibonachi()
        
        mock_print.assert_called_once_with(5)
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_invalid_input_shows_error(self, mock_secho, mock_print, mock_input):
        """Тест: невалидный ввод - показывается ошибка"""
        mock_input.side_effect = ['-5', 'back']
        
        fibonachi()
        
        mock_secho.assert_called_once()
        assert mock_secho.call_args[1]['fg'] == 'red'
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_exit_commands_work(self, mock_secho, mock_print, mock_input):
        """Тест: команды выхода работают"""
        for exit_cmd in ['back', 'b', 'q']:
            mock_input.side_effect = [exit_cmd]
            
            fibonachi()
            
            mock_print.assert_not_called()
            mock_secho.assert_not_called()

class TestFiboRec:
    def test_fibo_rec_positive_numbers(self):
        """Тест рекурсивной функции числа Фибоначчи для положительных чисел"""
        assert fibo_recursive(0) == 0
        assert fibo_recursive(1) == 1
        assert fibo_recursive(2) == 1
        assert fibo_recursive(3) == 2
        assert fibo_recursive(5) == 5
        assert fibo_recursive(7) == 13