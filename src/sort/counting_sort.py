import typer
from src.validation.sort_int_validation import sort_int_validation


def counting_sort()->None:
    """
    работает в режиме сортировки подсчетом

    :return: None
    """
    while (n:= input("Counting sort mode>> ")) not in ["back", 'b', 'q']:
        try:
            n_list = n.split()
            valid, message = sort_int_validation(n_list)
            if valid:
                print(*count(list(map(int, n_list))))
            else:
                typer.secho(message, fg=typer.colors.RED)
        except Exception as e:
            typer.secho(f"Error: {e}", fg=typer.colors.RED)


def count(a:list[int]) -> list[int]:
    """
    осуществляем сортировку подсчетом

    :param а: данный список, который надо отсортировать
    :return: а отсортированный список
    """

    if len(a)<=1:
        return a
    min_val = min(a)
    max_val = max(a)
    offset = -min_val
    count = [0] * (max_val - min_val + 1)
    for num in a:
        count[num + offset] += 1
    result = []
    for i in range(len(count)):
        result.extend([i - offset] * count[i])
    return result
