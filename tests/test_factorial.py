from unittest.mock import patch
from src.factorial import fac, fac_rec, factorial
    

class TestFactorialMode:
    """Тесты для режима факториала"""
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_valid_input_calculates_factorial(self, mock_secho, mock_print, mock_input):
        """Тест: валидный ввод - вычисляется факториал"""
        mock_input.side_effect = ['5', 'back']
        
        factorial()
        
        mock_print.assert_called_once_with(120)
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_invalid_input_shows_error(self, mock_secho, mock_print, mock_input):
        """Тест: невалидный ввод - показывается ошибка"""
        mock_input.side_effect = ['-5', 'back']
        
        factorial()
        
        mock_secho.assert_called_once()
        assert mock_secho.call_args[1]['fg'] == 'red'
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_exit_commands_work(self, mock_secho, mock_print, mock_input):
        """Тест: команды выхода работают"""
        for exit_cmd in ['back', 'b', 'q']:
            mock_input.side_effect = [exit_cmd]
            
            factorial()
            
            mock_print.assert_not_called()
            mock_secho.assert_not_called()

class TestFac:
    def test_fac_positive_numbers(self):
        """Тест итеративной функции факториала для положительных чисел"""
        assert fac(0) == 1
        assert fac(1) == 1
        assert fac(2) == 2
        assert fac(3) == 6
        assert fac(5) == 120
        assert fac(7) == 5040

class TestFactorialRecurciveMode:
    """Тесты работа мода реурсивного факториала"""
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_valid_input_calculates_factorial_rec(self, mock_secho, mock_print, mock_input):
        """Тест: валидный ввод - вычисляется факториал"""
        mock_input.side_effect = ['5', 'back']
        
        factorial()
        
        mock_print.assert_called_once_with(120)
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_invalid_input_shows_error(self, mock_secho, mock_print, mock_input):
        """Тест: невалидный ввод - показывается ошибка"""
        mock_input.side_effect = ['-5', 'back']
        
        factorial()
        
        mock_secho.assert_called_once()
        assert mock_secho.call_args[1]['fg'] == 'red'
    
    @patch('builtins.input')
    @patch('builtins.print')
    @patch('typer.secho')
    def test_exit_commands_work(self, mock_secho, mock_print, mock_input):
        """Тест: команды выхода работают"""
        for exit_cmd in ['back', 'b', 'q']:
            mock_input.side_effect = [exit_cmd]
            
            factorial()
            
            mock_print.assert_not_called()
            mock_secho.assert_not_called()

class TestFacRec:
    def test_fac_rec_positive_numbers(self):
        """Тест рекурсивной функции факториала для положительных чисел"""
        assert fac_rec(0) == 1
        assert fac_rec(1) == 1
        assert fac_rec(2) == 2
        assert fac_rec(3) == 6
        assert fac_rec(5) == 120
        assert fac_rec(7) == 5040