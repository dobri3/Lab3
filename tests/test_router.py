from unittest.mock import patch

from src.router import router


class TestRouter:
    """Тесты работа роутера"""
    @patch('typer.echo')
    @patch('typer.secho')
    def test_router_invalid(self, mock_secho, mock_echo):
        """Тест: инвалидный input"""
        router('unknown')
        mock_secho.assert_called_once_with("Unknown function: unknown", fg="red")

    @patch('typer.echo')
    @patch('typer.secho')
    def test_router_valid(self, mock_secho, mock_echo):
        """Тест: валидный input"""
        router('factorial')
        mock_echo.assert_called_once()
        call_args = mock_echo.call_args[0][0]
        assert 'Entering' in call_args and 'mode' in call_args
