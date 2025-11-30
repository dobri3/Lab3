import typer

from src.validation.fibo_factorial_validation import fibo_factorial_validation



def factorial() -> None:
    """
    работает в режиме вычисления факториала

    :return: None
    """

    while (n:= input("Factorial mode>> ")) not in ["back", 'b', 'q']:
        try:
            valid, message = fibo_factorial_validation(n)
            if valid:
                print(fac(int(n)))
            else:
                typer.secho(message, fg=typer.colors.RED)
        except Exception as e:
            typer.secho(f"Error: {e}", fg=typer.colors.RED)


def fac(n:int) -> int:

    """
    вычисляет факториал

    :param n: число, от которого вычисляется фактриал
    :return: ans - ответ
    """

    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    return ans



def factorial_recursive() -> None:
    """
    работает в режиме рекурсивного вычисления факториала

    :return: None
    """

    while (n:= input("Recursive factorial mode>> ")) not in ["back", 'b', 'q']:
        try:
            valid, message = fibo_factorial_validation(n)
            if valid:
                print(fac_rec(int(n)))
            else:
                typer.secho(message, fg=typer.colors.RED)
        except Exception as e:
            typer.secho(f"Error: {e}", fg=typer.colors.RED)

def fac_rec(n:int) -> int:
    """
    вычисляет факториал рекурсивно

    :param n: число, от которого вычисляется фактриал
    :return: ans - ответ
    """
    if n==0:
        return 1
    if n==1:
        return 1
    else:
        return n * fac_rec(n-1)
