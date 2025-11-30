from math import sqrt

import typer

from src.validation.fibo_factorial_validation import fibo_factorial_validation




def fibonachi() -> None:
    """
    работает в режиме вычисления числа Фибоначчи

    :return: None
    """

    while (n:= input("Fibonachi mode>> ")) not in ["back", 'b', 'q']:
        try:
            valid, message = fibo_factorial_validation(n)
            if valid:
                print(fibo(int(n)))
                # typer echo???
            else:  
                typer.secho(message, fg=typer.colors.RED)
        except Exception as e:
            typer.secho(f"Error: {e}", fg=typer.colors.RED)

def fibo(n:int)-> int:
    """
    вычисляет число Фибоначчи

    :param n: число, от которого вычисляется число Фибоначчи 
    :return: ans - ответ
    """
    
    f = ((1+(5**0.5))**n - (1-(5**0.5))**n)/((2**n) * (5**0.5))
    return int(f)

def fibonachi_recursive() -> None:
    """
    работает в режиме вычисления числа Фибоначчи рекурсивно

    :return: None
    """

    while (n:= input("Recursive Fibonachi mode>> ")) not in ["back", 'b', 'q']:
        try:
            valid, message = fibo_factorial_validation(n)
            if valid:
                print(fibo_recursive(int(n)))
            else:  
                typer.secho(message, fg=typer.colors.RED)
        except Exception as e:
            typer.secho(f"Error: {e}", fg=typer.colors.RED)

def fibo_recursive(n:int)-> int:
    """
    вычисляет рекурсивное число Фибоначчи

    :param n: число, от которого вычисляется рекурсивное число Фибоначчи 
    :return: ans - ответ
    """
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)
    
