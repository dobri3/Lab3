import typer
from src.validation.sort_int_validation import sort_int_validation


def quick_sort() -> None:
    """
    работает в режиме быстрой сортировки

    :return: None
    """

    while (n:= input("Quick sort mode>> ")) not in ["back", 'b', 'q']:
        try:
            n = n.split()
            valid, message = sort_int_validation(n)
            if valid:
                n = list(map(int, n))
                print(*quick(n))
            else:  
                typer.secho(message, fg=typer.colors.RED)
        except Exception as e:
            typer.secho(f"Error: {e}", fg=typer.colors.RED)


def quick(a:list[int]) -> list[int]:
    """
    осуществляем быструю сортировку

    :param а: данный список, который надо отсортировать
    :return: а отсортированный список
    """
    if len(a) <= 1:
        return a
    else:
        pivot = a[len(a) // 2]
        less = [x for x in a if x < pivot]
        equal = [x for x in a if x == pivot]
        greater = [x for x in a if x > pivot]
        return quick(less) + equal + quick(greater)