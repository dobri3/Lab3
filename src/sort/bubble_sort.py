import typer

from src.validation.sort_int_validation import sort_int_validation

def bubble_sort() -> None:
    """
    работает в режиме сортировки пузырьком

    :return: None
    """

    while (n:= input("Bubble sort mode>> ")) not in ["back", 'b', 'q']:
        try:
            n_list = n.split()
            valid, message = sort_int_validation(n_list)
            if valid:
                print(*bubble(list(map(int, n_list))))
            else:
                typer.secho(message, fg=typer.colors.RED)
        except Exception as e:
            typer.secho(f"Error: {e}", fg=typer.colors.RED)


def bubble(a:list[int]) -> list[int]:
    """
    осуществляем сортировку пузырьком

    :param а: данный список, который надо отсортировать
    :return: а отсортированный список
    """
    n = len(a)
    for i in range(n):
        for j in range(0, n - i -1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
