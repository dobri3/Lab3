import typer
from src.constants import HANDLERS


def router(fucntion_input: str)-> None:
    """
    обрабатывает поступившие команды, и направляет пользователя на ту команду, которую он ввел 

    :param fucntion_input: функция, на которую нужно переключиться
    :return: None
    """
    
    handler = HANDLERS.get(fucntion_input)
    
    if not handler:
        typer.secho(f"Unknown function: {fucntion_input}", fg="red")
        return
        
    typer.echo(f"Entering {fucntion_input} mode. Type 'back','b' or 'q' to return to function selection.")
    
    try:
        handler()
    except Exception as e:
        typer.secho(f"Error: {e}",  fg="red")