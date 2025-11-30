import typer
from src.validation.sort_int_validation import sort_int_validation


def radix_sort()->None:
    """
    работает в режиме radix сортировки

    :return: None
    """
    while (n:= input("Radix sort mode>> ")) not in ["back", 'b', 'q']:
        try:
            n_list = n.split()
            valid, message = sort_int_validation(n_list)
            if valid:
                print(*radix(list(map(int, n_list))))
            else:
                typer.secho(message, fg=typer.colors.RED)
        except Exception as e:
            typer.secho(f"Error: {e}", fg=typer.colors.RED)


def radix(a:list[int], base: int = 10) -> list[int]:
    """
    осуществляем radix cортировку

    :param а: данный список, который надо отсортировать
    :return: а отсортированный список
    """
    if len(a)<=1:
        return a
    max_len = max([len(str(abs(x))) for x in a])
    cells:list[list[int]] = [[] for _ in range(base)]
    for i in range(0, max_len):
        for x in a:
            digit = (x // base ** i) % base
            cells[digit].append(x)
        array:list[int] = [x for queue in cells for x in queue]
        cells = [[] for _ in range(base)]

    negatives = [x for x in array if x < 0]
    positives = [x for x in array if x >= 0]

    return negatives + positives
